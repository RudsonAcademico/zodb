"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-17896.c345.samerica-east1-1.gce.redns.redis-cloud.com',
    port=17896,
    decode_responses=True,
    username="default",
    password="1xHBdfloqmO6YvAOHIS7bw1XEw8sxvMs",
)

class Usuario:
    def __init__(self, user_id, email, nome, senha):
        self.user_id = user_id
        self.email = email
        self.nome = nome
        self.senha = senha
    def salvar(self):
        r.hset(f'user:{self.user_id}', mapping={
            'email': self.email,
            'nome': self.nome,
            'senha': self.senha
        })
    def get(user_id):
        dados = r.hgetall(f'user:{user_id}')
        if dados:
            return Usuario(user_id, dados.get('email'), dados.get('nome'), dados.get('senha'))


# r.set(f'user:{self.user_id}:email', self.email)
# r.set(f'user:{self.user_id}:nome', self.nome)
# r.set(f'user:{self.user_id}:senha', self.senha)

# email = r.get(f'user:{user_id}:email')
# nome = r.get(f'user:{user_id}:nome')
# senha = r.get(f'user:{user_id}:senha')
# if email and nome and senha:
#     usuario = Usuario(user_id, email, nome, senha)

print(r.info())
