num = input('Digite um numero de 1 a 9999: ')

if len(num) > 3:
    uni = num[3]
    dezena = num[2]
    centena = num[1]
    milhar = num[0]

    print('Unidade: ', uni)
    print('dezena: ', dezena)
    print('centena: ', centena)
    print('milhar: ', milhar)
else:
    print('o numero não é milhar')


