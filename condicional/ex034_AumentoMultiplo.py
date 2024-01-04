salario = float(input('Digite seu salario: '))

if salario > 1250:
    aumento = salario * 0.10
    print('O salario total do colaborador é de: {:.2f} R$'.format(salario + aumento))
else:
    aumento = salario * 0.15
    print('O salario total do colaborador é de: {:.2f} R$'.format(salario + aumento))