def calculadora():
    print('-------------------------------------')
    print('             Calculadora             ')
    print('-------------------------------------')

    while True:
        try:
            acao = int(input('\nEscolha o número da operação: \n1 - Soma\n2 - Subtração\n3 - Divisão\n4 - Multiplicação\n0 - Sair\nOpção: '))
            if acao == 0:
                print("Encerrando a calculadora.")
                break

            numero1 = float(input('Digite o primeiro número: '))
            numero2 = float(input('Digite o segundo número: '))

            match acao:
                case 1:
                    print(f"Resultado: {numero1 + numero2}")
                case 2:
                    print(f"Resultado: {numero1 - numero2}")
                case 3:
                    if numero2 == 0:
                        print("Erro: divisão por zero.")
                    else:
                        print(f"Resultado: {numero1 / numero2}")
                case 4:
                    print(f"Resultado: {numero1 * numero2}")
                case _:
                    print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")

calculadora()