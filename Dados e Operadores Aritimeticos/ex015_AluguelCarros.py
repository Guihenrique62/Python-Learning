kilometragem = float(input('Digite a quantidade de KM percorridos: '))
dias = int(input('Digite a quantidade de dias alugado: '))

preco = dias * 60 + (0.15 * kilometragem)

print('O preço final do carro é de: {} R$'.format(preco))