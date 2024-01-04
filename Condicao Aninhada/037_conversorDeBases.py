num = int(input('Digite o numero:'))

choice = int(input('Escolha para o que quer converter: \n [1] - Binario\n [2] - Octal\n [3] - Hexadecimal'))

match choice:
    case 1:
        print(bin(num))
    case 2:
        print(oct(num))
    case 3:
        print(hex(num))