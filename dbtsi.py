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

r.set('chave', 0)
print(r.get('chave'))
print(r.exists('chave'))
r.delete('chave')
print(r.exists('chave'))
r.set('chave', 0)
r.incr('chave')      # +1
print(r.get('chave'))
r.incrby('chave', 5) # +5
print(r.get('chave'))
r.decr('chave')      # -1
print(r.get('chave'))
r.decrby('chave', 5) # -5
print(r.get('chave'))