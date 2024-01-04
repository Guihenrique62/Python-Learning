car_velocity = float(input('Digite a velocidade do carro: '))

if car_velocity > 80:
    multa = (car_velocity - 80) * 7.00
    print('Você foi multado, no valor de {:.2f} R$'.format(multa))
else:
    print('Voce não foi multado')