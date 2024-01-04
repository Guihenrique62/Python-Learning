phrase = input('Digite uma frase: ').strip()

print('A letra A aparece {} vezes na Frase'.format(phrase.upper().count('A')))
print('A primeira letra A aparece na posição {}'.format(phrase.upper().find('A')+1))
print('A ultima letra A aparece na posição {}'.format(phrase.upper().rfind('A') + 1))
