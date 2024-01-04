value_home = float(input('Digite o valor total da casa: '))
salario = float(input('Digite o se salario: '))
ano_parcela = int(input('Digite a quantidade de anos que irá ser pago: '))

parcela = value_home / (ano_parcela * 12)
percent_salario = salario * 0.30

if parcela > percent_salario:
    print('A parcela vale mais do que seu salário pode pagar!')
else:
    print('A Parcela ficou em um total de {} R$. Como deseja pagar?'.format(parcela))