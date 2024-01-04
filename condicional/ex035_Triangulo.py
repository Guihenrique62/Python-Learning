r1 = float(input('Primeiro Seguimento: '))
r2 = float(input('segundo Seguimento: '))
r3 = float(input('terceiro Seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+r2:
    print('os seguimentos acima podem formar triangulo!')
else:
    print('os seguimentos acima não podem formar triangulo!')
