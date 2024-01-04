km = float(input('Digite a quantidade de Km: '))

if km <= 200:
    print('O valor da passagem é {:.2f} RS'.format(km * 0.50))
else:
    print('O valor da passagem é {:.2f} RS'.format(km * 0.45))