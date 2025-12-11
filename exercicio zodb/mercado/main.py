from model import Produto, Estoque
from ZODB import DB, FileStorage
import transaction

print("--- Sistema de Gerenciamento de Estoque ---\n1. Adicionar novo produto\n2. Buscar produto por nome\n3. Listar todos os produtos\n4. Adicionar ou Remover quantidade de um produto\n5. Remover produto do estoque\n0. Sair")
requisito = int(input("Escolha uma opção: "))
storage = FileStorage.FileStorage('estoque.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

if 'estoque' not in root:
    root.estoque = Estoque()
estoque = root.estoque

while requisito != 0:
    if requisito == 1:
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade inicial: "))

        try:
            estoque.adicionar_produto(nome, quantidade)
            transaction.commit()
            print("Produto adicionado com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 2:
        nome = input("Digite o nome do produto a buscar: ")
        estoque.buscar_produto(nome)
        input("Pressione Enter para continuar...")

    elif requisito == 3:
        estoque.listar_todos_produtos()
        input("Pressione Enter para continuar...")

    elif requisito == 4:
        nome = input("Digite o nome do produto: ")
        alteracao = int(input("Digite a quantidade a adicionar (use negativo para remover): "))

        try:
            estoque.atualizar_estoque(nome, alteracao)
            transaction.commit()
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    elif requisito == 5:
        nome = input("Digite o nome do produto a remover: ")

        try:
            estoque.remover_produto(nome)
            transaction.commit()
            print("Produto removido com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")

    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")
    
    print("\n--- Sistema de Gerenciamento de Estoque ---\n1. Adicionar novo produto\n2. Buscar produto por nome\n3. Listar todos os produtos\n4. Adicionar ou Remover quantidade de um produto\n5. Remover produto do estoque\n0. Sair")
    requisito = int(input("Escolha uma opção: "))