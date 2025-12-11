import persistent

class Produto(persistent.Persistent):
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque(persistent.Persistent):
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, nome, quantidade):
        """
        solicita ao usuário o nome e a quantidade inicial de um produto e o armazena no banco de dados.
        O sistema deve impedir a adição de produtos com nomes duplicados.
        """
        for produto in self.produtos:
            if produto.nome == nome:
                raise ValueError("Produto com nome duplicado não pode ser adicionado.")
        novo_produto = Produto(nome, quantidade)
        self.produtos.append(novo_produto)

    def buscar_produto(self, nome):
        """
        solicita o nome de um produto e exibe seus detalhes (nome e quantidade) caso seja encontrado.
        """
        for produto in self.produtos:
            if produto.nome == nome:
                print(f"Produto encontrado: Nome: {produto.nome}, Quantidade: {produto.quantidade}")
                return
        print("Produto não encontrado.")
    
    def listar_todos_produtos(self):
        """
        exibe uma lista de todos os produtos cadastrados e suas respectivas quantidades.
        """
        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return
        print("Lista de todos os produtos:")
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Quantidade: {produto.quantidade}")
    
    def atualizar_estoque(self, nome, alteracao):
        """
        solicita o nome de um produto e uma quantidade a ser adicionada ou removida do estoque.
        O sistema deve validar a operação para não permitir que o estoque se torne negativo.
        """
        for produto in self.produtos:
            if produto.nome == nome:
                if produto.quantidade + alteracao < 0:
                    raise ValueError("Operação inválida: Estoque não pode ser negativo.")
                produto.quantidade += alteracao
                print(f"Estoque atualizado: Nome: {produto.nome}, Nova Quantidade: {produto.quantidade}")
                return
        print("Produto não encontrado.")
    
    def remover_produto(self, nome):
        """
        solicita o nome de um produto e o exclui permanentemente do banco de dados.
        """
        for produto in self.produtos:
            if produto.nome == nome:
                print(f"Produto removido: Nome: {produto.nome}")
                self.produtos.remove(produto)
                return
        print("Produto não encontrado.")