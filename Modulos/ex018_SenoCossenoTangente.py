from math import sin,cos,tan,radians
ang = float(input('Digite um angulo qualquer: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O seno de {} é {:.2f} '.format(ang,seno))
print('O coseno de {} é {:.2f} '.format(ang,coseno))
print('A tangente de {} é {:.2f} '.format(ang,tangente))


