import persistent

class Produto(persistent.Persistent):
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque(persistent.Persistent):
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        for produto in self.produtos:
            if produto.nome == nome:
                raise ValueError("Produto com nome duplicado não pode ser adicionado.")
        novo_produto = Produto(nome, quantidade)
        self.produtos.append(novo_produto)

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                print(f"Produto encontrado: Nome: {produto.nome}, Quantidade: {produto.quantidade}")
                return
        print("Produto não encontrado.")
    
    def listar_todos_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("Lista de todos os produtos:")
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Quantidade: {produto.quantidade}")
    
    def atualizar_estoque(self, nome, alteracao):
        for produto in self.produtos:
            if produto.nome == nome:
                if produto.quantidade + alteracao < 0:
                    raise ValueError("Operação inválida: Estoque não pode ser negativo.")
                produto.quantidade += alteracao
                print(f"Estoque atualizado: Nome: {produto.nome}, Nova Quantidade: {produto.quantidade}")
                return
        print("Produto não encontrado.")
    
    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                print(f"Produto removido: Nome: {produto.nome}")
                self.produtos.remove(produto)
                return
        print("Produto não encontrado.")