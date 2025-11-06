from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Produto, Usuario, Pedido
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'exercicios.db')
DB_URL = f'sqlite:///{DB_PATH}'

""""
Função: all()
1. Liste todos os produtos cadastrados no sistema.
2. Recupere todos os usuários ativos com mais de 18 anos.
3. Obtenha todos os pedidos feitos depois de 01/03/2025 com quantidade superior a 5.
"""
def listar_produtos():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Lista de Produtos:")
    try:
        produtos = session.query(Produto).all()
        if not produtos:
            print('Nenhum produto cadastrado.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

def listar_usuarios_ativos_maiores():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nUsuários Ativos com mais de 18 anos:")
    try: 
        usuarios = session.query(Usuario).filter(Usuario.ativo == True, Usuario.idade > 18).all()
        if not usuarios:
            print('Nenhum usuário ativo maior de 18 anos encontrado.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_pedidos_filtrados():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nPedidos feitos depois de 01/03/2025 com quantidade superior a 5:")
    try:
        pedidos = session.query(Pedido).filter(
            Pedido.data_pedido > datetime(2025, 3, 1),
            Pedido.quantidade > 5
        ).all()
        if not pedidos:
            print('Nenhum pedido encontrado com os critérios especificados.')
            return
        for ped in pedidos:
            print(f"Pedido ID: {ped.id}, Usuário ID: {ped.usuario_id}, Produto ID: {ped.produto_id}, Quantidade: {ped.quantidade}, Data do Pedido: {ped.data_pedido}")
    finally:
        session.close()

"""
Função: first()

4. Encontre o primeiro usuário cadastrado no sistema.
5. Verifique qual é o produto mais barato da categoria "eletrônicos".
6. Determine o último pedido realizado por qualquer usuário.
"""

def primeiro_usuario_cadastrado():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nPrimeiro usuário cadastrado no sistema:")
    try:
        usuario = session.query(Usuario).order_by(Usuario.id).first()
        if usuario:
            print(f"nome: {usuario.nome}, email: {usuario.email}, idade: {usuario.idade}, ativo: {usuario.ativo}")
        else:
            print('Nenhum usuário cadastrado.')
    finally:
        session.close()

def produto_mais_barato_eletronicos():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nProduto mais barato da categoria 'eletrônicos':")
    try:
        produto = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco).first()
        if produto:
            print(f"nome: {produto.nome}, preço: {produto.preco}, categoria: {produto.categoria}, estoque: {produto.estoque}")
        else:
            print('Nenhum produto encontrado na categoria "eletrônicos".')
    finally:
        session.close()

def ultimo_pedido_realizado():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nÚltimo pedido realizado por qualquer usuário:")
    try:
        pedido = session.query(Pedido).order_by(Pedido.data_pedido.desc()).first()
        if pedido:
            print(f"Pedido ID: {pedido.id}, Usuário ID: {pedido.usuario_id}, Produto ID: {pedido.produto_id}, Quantidade: {pedido.quantidade}, Data do Pedido: {pedido.data_pedido}")
        else:
            print('Nenhum pedido realizado.')
    finally:
        session.close()

if __name__ == '__main__':
    print("Executando consultas com SQLAlchemy ORM...\n")
    print("Exercício: all()")
    listar_produtos()
    listar_usuarios_ativos_maiores()
    listar_pedidos_filtrados()
    print("\nExercício: first()")
    primeiro_usuario_cadastrado()
    produto_mais_barato_eletronicos()
    ultimo_pedido_realizado()
    
