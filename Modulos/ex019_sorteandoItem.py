import random
pessoa1 = input('Digite o nome de uma pessoa: ')
pessoa2 = input('Digite o nome de uma pessoa: ')
pessoa3 = input('Digite o nome de uma pessoa: ')
pessoa4 = input('Digite o nome de uma pessoa: ')

list = [pessoa1,pessoa2,pessoa3,pessoa4]

escolhido = random.choice(list)
print('A pessoa escolhida foi: {}'.format(escolhido))