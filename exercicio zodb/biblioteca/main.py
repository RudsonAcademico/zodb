from model import Biblioteca, Livro, Usuario
from ZODB import DB, FileStorage
import transaction

print("--- Sistema de Gerenciamento de Biblioteca ---\n1. Cadastrar novo livro\n2. Cadastrar novo usuário\n3. Registrar empréstimo de livro\n4. Registrar devolução de livro\n5. Listar todos os livros\n6. Listar todos os usuários\n0. Sair")
requisito = int(input("Escolha uma opção: "))
storage = FileStorage.FileStorage('biblioteca.fs')
db = DB(storage)
connection = db.open()
root = connection.root()

if 'biblioteca' not in root:
    root.biblioteca = Biblioteca()
biblioteca = root.biblioteca

while requisito != 0:
    if requisito == 1:
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")

        try:
            biblioteca.cadastrar_livro(titulo, autor)
            transaction.commit()
            print("Livro cadastrado com sucesso.")
            input("Pressione Enter para continuar...")

        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 2:
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
    
        try:
            biblioteca.cadastrar_usuario(nome, email)
            transaction.commit()
            print("Usuário cadastrado com sucesso.")
            input("Pressione Enter para continuar...")
    
        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 3:
        titulo = input("Digite o título do livro a ser emprestado: ")
        email = input("Digite o email do usuário que está pegando o livro: ")
    
        try:
            biblioteca.registrar_emprestimo(titulo, email)
            transaction.commit()
            input("Pressione Enter para continuar...")
    
        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 4:
        titulo = input("Digite o título do livro a ser devolvido: ")
    
        try:
            biblioteca.registrar_devolucao(titulo)
            transaction.commit()
            input("Pressione Enter para continuar...")
    
        except ValueError as e:
            print(e)
            input("Pressione Enter para continuar...")
    
    elif requisito == 5:
        biblioteca.listar_livros()
        input("Pressione Enter para continuar...")
    
    elif requisito == 6:
        biblioteca.listar_usuarios()
        input("Pressione Enter para continuar...")
    
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")

    
    print("\n--- Sistema de Gerenciamento de Biblioteca ---\n1. Cadastrar novo livro\n2. Cadastrar novo usuário\n3. Registrar empréstimo de livro\n4. Registrar devolução de livro\n5. Listar todos os livros\n6. Listar todos os usuários\n0. Sair")
    requisito = int(input("Escolha uma opção: "))