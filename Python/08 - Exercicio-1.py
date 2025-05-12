nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'Seu nome eh {nome}')
    print(f'Sua idade eh {idade}')
    print(f'Seu nome invertido eh: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espacos')
    else:
        print('Seu nome nao contem espacos')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome eh {nome[0]}')
    print(f'A ultima letra do seu nome eh {nome[-1]}')
else:
    print('Desculpe, edu erro ai')