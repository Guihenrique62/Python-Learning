value = input('Digite Algo: ')

print('O tipo primitivo deste valor é: ', type(value))
print('Só tem Espaços? ', value.isspace())
print('É um numero?', value.isnumeric())
print('É Alfabético?', value.isalpha())
print('É Alfanumerico ', value.isalnum())
print('Está em maiúsculas? ', value.isupper())
print('Está em minusculas?', value.islower())
