import random
choice_user = int(input('Digite a sua escolha: \n 1 - Pedra\n 2 - Papel\n 3 - Tesoura'))
choice_sys = random.randrange(1,4)
choice_sys_write = ''

match choice_sys:
    case 1:
        choice_sys_write = 'Pedra'
    case 2:
        choice_sys_write = 'Papel'
    case 3:
        choice_sys_write = 'Tesoura'


if choice_user == choice_sys:
    print('O sistema escolheu {}'.format(choice_sys_write))
    print('=<'*10)
    print('Deu empate!')
elif choice_user == 1 and choice_sys == 2:
    print('O sistema escolheu {}'.format(choice_sys_write))
    print('=<'*10)
    print('Voce Perdeu!')
elif choice_user == 2 and choice_sys == 3:
    print('O sistema escolheu {}'.format(choice_sys_write))
    print('=<'*15)
    print('Voce Perdeu!')
elif choice_user == 3 and choice_sys == 1:
    print('O sistema escolheu {}'.format(choice_sys_write))
    print('=<'*10)
    print('Voce Perdeu!')
else:
    print('O sistema escolheu {}'.format(choice_sys_write))
    print('=<' * 10)
    print('Voce Ganhou!')