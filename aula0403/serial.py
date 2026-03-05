21:10
import hashlib
import itertools
import string

hash_alvo = "ca6ae33116b93e57b87810a27296fc36"

contador = 0

for tentativa in itertools.product(string.digits, repeat=9):
senha = ''.join(tentativa)
contador += 1

if contador % 1000000 == 0:
print("Testadas:", contador)

if hashlib.md5(senha.encode()).hexdigest() == hash_alvo:
print("Senha encontrada:", senha)
break