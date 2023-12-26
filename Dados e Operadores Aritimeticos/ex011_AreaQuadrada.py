largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da Parede: '))

area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m2'.format(altura,largura,area))
print('Para pintar esta parede você irá precisar de {:.3f} Litros de Tinta'.format(tinta))
