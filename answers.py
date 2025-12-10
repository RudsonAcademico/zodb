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

"""
Função: get(pk)
7. Recupere os dados completos do usuário com ID 7.
8. Verifique se existe um produto com ID 5 e estoque positivo.
9. Obtenha o pedido de ID 3 junto com os dados do usuário associado.
"""

def get_usuario_por_id(usuario_id):
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(f"\nDados do usuário com ID {usuario_id}:")
    try:
        usuario = session.get(Usuario, usuario_id)
        if usuario:
            print(f"nome: {usuario.nome}, email: {usuario.email}, idade: {usuario.idade}, ativo: {usuario.ativo}")
        else:
            print(f'Usuário com ID {usuario_id} não encontrado.')
    finally:
        session.close()

def get_produto_estoque_positivo(produto_id):
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(f"\nVerificação do produto com ID {produto_id} e estoque positivo:")
    try:
        produto = session.get(Produto, produto_id)
        if produto and produto.estoque > 0:
            print(f"nome: {produto.nome}, preço: {produto.preco}, categoria: {produto.categoria}, estoque: {produto.estoque}")
        else:
            print(f'Produto com ID {produto_id} não encontrado ou sem estoque positivo.')
    finally:
        session.close()

def get_pedido_com_usuario(pedido_id):
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print(f"\nDados do pedido com ID {pedido_id} e usuário associado:")
    try:
        pedido = session.get(Pedido, pedido_id)
        if pedido:
            usuario = pedido.usuario
            print(f"Pedido ID: {pedido.id}, Usuário: {usuario.nome}, Produto ID: {pedido.produto_id}, Quantidade: {pedido.quantidade}, Data do Pedido: {pedido.data_pedido}")
        else:
            print(f'Pedido com ID {pedido_id} não encontrado.')
    finally:
        session.close()

"""
Função: filter()
10. Encontre usuários com idade entre 25 e 35 anos.
11. Liste pedidos com status "cancelado" ou "pendente" feitos depois de 2024.
12. Selecione produtos com preço acima de R$ 500 que tiveram pelo menos 1 pedido.
"""

def listar_usuarios_idade_25_35():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nUsuários com idade entre 25 e 35 anos:")
    try:
        usuarios = session.query(Usuario).filter(Usuario.idade.between(25, 35)).all()
        if not usuarios:
            print('Nenhum usuário encontrado na faixa etária especificada.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_pedidos_status_data():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nPedidos com status 'cancelado' ou 'pendente' feitos depois de 2024:")
    try:
        pedidos = session.query(Pedido).filter(
            Pedido.status.in_(['cancelado', 'pendente']),
            Pedido.data_pedido > datetime(2024, 1, 1)
        ).all()
        if not pedidos:
            print('Nenhum pedido encontrado com os critérios especificados.')
            return
        for ped in pedidos:
            print(f"Pedido ID: {ped.id}, Usuário ID: {ped.usuario_id}, Produto ID: {ped.produto_id}, Quantidade: {ped.quantidade}, Status: {ped.status}, Data do Pedido: {ped.data_pedido}")
    finally:
        session.close()

def listar_produtos_preco_pedidos():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nProdutos com preço acima de R$ 500 que tiveram pelo menos 1 pedido:")
    try:
        produtos = session.query(Produto).join(Pedido).filter(Produto.preco > 500).all()
        if not produtos:
            print('Nenhum produto encontrado com os critérios especificados.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

"""
Função: filter_by()
13. Busque todos os usuários com status inativo.
14. Encontre produtos da categoria "livros" com preço inferior a R$ 100.
15. Obtenha os 3 produtos mais caros com estoque disponível.
"""

def listar_usuarios_inativos():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nUsuários inativos:")
    try:
        usuarios = session.query(Usuario).filter_by(ativo=False).all()
        if not usuarios:
            print('Nenhum usuário inativo encontrado.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_produtos_livros_preco_inferior():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nProdutos da categoria 'livros' com preço inferior a R$ 100:")
    try:
        produtos = session.query(Produto).filter_by(categoria='livros').filter(Produto.preco < 100).all()
        if not produtos:
            print('Nenhum produto encontrado na categoria "livros" com preço inferior a R$ 100.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

def listar_produtos_mais_caros_estoque():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\n3 produtos mais caros com estoque disponível:")
    try:
        produtos = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco.desc()).limit(3).all()
        if not produtos:
            print('Nenhum produto com estoque disponível encontrado.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()


"""
Função: order_by()
16. Liste todos os usuários em ordem alfabética de nome.
17. Ordene os produtos do mais caro para o mais barato.
18. Organize os pedidos por por status e depois data de criação (mais recentes primeiro).
"""

def listar_usuarios_ordenados_nome():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nUsuários em ordem alfabética de nome:")
    try:
        usuarios = session.query(Usuario).order_by(Usuario.nome).all()
        if not usuarios:
            print('Nenhum usuário cadastrado.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_produtos_ordenados_preco():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nProdutos do mais caro para o mais barato:")
    try:
        produtos = session.query(Produto).order_by(Produto.preco.desc()).all()
        if not produtos:
            print('Nenhum produto cadastrado.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

def listar_pedidos_ordenados_status_data():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nPedidos organizados por status e depois data de criação (mais recentes primeiro):")
    try:
        pedidos = session.query(Pedido).order_by(Pedido.status, Pedido.data_pedido.desc()).all()
        if not pedidos:
            print('Nenhum pedido cadastrado.')
            return
        for ped in pedidos:
            print(f"Pedido ID: {ped.id}, Usuário ID: {ped.usuario_id}, Produto ID: {ped.produto_id}, Quantidade: {ped.quantidade}, Status: {ped.status}, Data do Pedido: {ped.data_pedido}")
    finally:
        session.close()

"""
Função: limit(n)
19. Liste os 6 primeiros usuários cadastrados no sistema.
20. Obtenha os 5 produtos mais baratos disponíveis no estoque.
21. Selecione os 3 pedidos mais recentes feitos por usuários com idade maior que 30 anos.
"""

def listar_usuarios_limitados():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\n6 primeiros usuários cadastrados no sistema:")
    try:
        usuarios = session.query(Usuario).limit(6).all()
        if not usuarios:
            print('Nenhum usuário cadastrado.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_produtos_mais_baratos_estoque():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\n5 produtos mais baratos disponíveis no estoque:")
    try:
        produtos = session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco).limit(5).all()
        if not produtos:
            print('Nenhum produto com estoque disponível encontrado.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

def listar_pedidos_recentes_usuarios_maiores_30():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\n3 pedidos mais recentes feitos por usuários com idade maior que 30 anos:")
    try:
        pedidos = session.query(Pedido).join(Usuario).filter(Usuario.idade > 30).order_by(Pedido.data_pedido.desc()).limit(3).all()
        if not pedidos:
            print('Nenhum pedido encontrado para usuários com idade maior que 30 anos.')
            return
        for ped in pedidos:
            print(f"Pedido ID: {ped.id}, Usuário ID: {ped.usuario_id}, Produto ID: {ped.produto_id}, Quantidade: {ped.quantidade}, Data do Pedido: {ped.data_pedido}")
    finally:
        session.close()

"""
Função: offset(n)
22. Liste os usuários cadastrados, ignorando os 5 primeiros resultados.
23. Obtenha os produtos mais caros, pulando os 3 primeiros resultados na ordenação por preço.
24. Liste os pedidos realizados, ignorando os 8 primeiros, mas ordenados pela data de criação de forma decrescente.
"""

def listar_usuarios_ignorando_5_primeiros():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nUsuários cadastrados, ignorando os 5 primeiros resultados:")
    try:
        usuarios = session.query(Usuario).offset(5).all()
        if not usuarios:
            print('Nenhum usuário encontrado após ignorar os 5 primeiros.')
            return
        for u in usuarios:
            print(f"nome: {u.nome}, email: {u.email}, idade: {u.idade}, ativo: {u.ativo}")
    finally:
        session.close()

def listar_produtos_caros_ignorando_3_primeiros():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nProdutos mais caros, pulando os 3 primeiros resultados na ordenação por preço:")
    try:
        produtos = session.query(Produto).order_by(Produto.preco.desc()).offset(3).all()
        if not produtos:
            print('Nenhum produto encontrado após ignorar os 3 primeiros mais caros.')
            return
        for p in produtos:
            print(f"nome: {p.nome}, preço: {p.preco}, categoria: {p.categoria}, estoque: {p.estoque}")
    finally:
        session.close()

def listar_pedidos_ignorando_8_primeiros():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nPedidos realizados, ignorando os 8 primeiros, ordenados pela data de criação de forma decrescente:")
    try:
        pedidos = session.query(Pedido).order_by(Pedido.data_pedido.desc()).offset(8).all()
        if not pedidos:
            print('Nenhum pedido encontrado após ignorar os 8 primeiros.')
            return
        for ped in pedidos:
            print(f"Pedido ID: {ped.id}, Usuário ID: {ped.usuario_id}, Produto ID: {ped.produto_id}, Quantidade: {ped.quantidade}, Data do Pedido: {ped.data_pedido}")
    finally:
        session.close()

"""
Função: count()
25. Conte quantos usuários estão cadastrados no sistema.
26. Determine o número de pedidos realizados com status "entregue".
27. Conte quantos produtos existem na categoria "eletrônicos" com estoque maior que 0 e preço acima de R$ 100,00.
"""

def contar_usuarios_cadastrados():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nNúmero total de usuários cadastrados no sistema:")
    try:
        total_usuarios = session.query(Usuario).count()
        print(f"Total de usuários cadastrados: {total_usuarios}")
    finally:
        session.close()

def contar_pedidos_entregues():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nNúmero de pedidos realizados com status 'entregue':")
    try:
        total_pedidos_entregues = session.query(Pedido).filter(Pedido.status == 'entregue').count()
        print(f"Total de pedidos entregues: {total_pedidos_entregues}")
    finally:
        session.close()

def contar_produtos_eletronicos_estoque_preco():
    engine = create_engine(DB_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("\nNúmero de produtos na categoria 'eletrônicos' com estoque maior que 0 e preço acima de R$ 100,00:")
    try:
        total_produtos = session.query(Produto).filter(
            Produto.categoria == 'eletrônicos',
            Produto.estoque > 0,
            Produto.preco > 100.00
        ).count()
        print(f"Total de produtos eletrônicos com estoque > 0 e preço > R$ 100,00: {total_produtos}")
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
    
    print("\nExercício: get(pk)")
    get_usuario_por_id(7)
    get_produto_estoque_positivo(5)
    get_pedido_com_usuario(3)
    
    print("\nExercício: filter()")
    listar_usuarios_idade_25_35()
    listar_pedidos_status_data()
    listar_produtos_preco_pedidos()
    
    print("\nExercício: filter_by()")
    listar_usuarios_inativos()
    listar_produtos_livros_preco_inferior()
    listar_produtos_mais_caros_estoque()
    
    print("\nExercício: order_by()")
    listar_usuarios_ordenados_nome()
    listar_produtos_ordenados_preco()
    listar_pedidos_ordenados_status_data()
    
    print("\nExercício: limit(n)")
    listar_usuarios_limitados()
    listar_produtos_mais_baratos_estoque()
    listar_pedidos_recentes_usuarios_maiores_30()
    
    print("\nExercício: offset(n)")
    listar_usuarios_ignorando_5_primeiros()
    listar_produtos_caros_ignorando_3_primeiros()
    listar_pedidos_ignorando_8_primeiros()

    print("\nExercício: count()")
    contar_usuarios_cadastrados()
    contar_pedidos_entregues()
    contar_produtos_eletronicos_estoque_preco()


