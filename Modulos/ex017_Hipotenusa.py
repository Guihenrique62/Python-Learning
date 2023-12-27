cat_oposto = float(input('Digite o comprimento do cateto oposto: '))
cat_adjas = float(input('Digite o comprimento do cateto adjascente: '))

hipotenusa = (cat_oposto **2 + cat_adjas ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))