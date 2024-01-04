import random

num_usuario = int(input('Digite um numero inteiro de 0 a 5: '))
num_sistema = random.randrange(0,6)

if num_usuario == num_sistema:
    print('Voce acertou o numero!')
else:
    print('Você perdeu!')