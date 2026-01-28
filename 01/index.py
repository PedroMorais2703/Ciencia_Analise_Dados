print('Calculadora simples')
primeiroNumero = input("Digite um numero: ")
segundoNumero = input("Digite outro numero: ")

num1 = float(primeiroNumero)
num2 = float(segundoNumero)

while True:
        print("Escolha a operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        escolha = input("Digite o número da operação (0 a 4): ")

        if escolha == '1':
                print(num1 + num2)
        elif escolha == '2':
                print(num1 - num2)
        elif escolha == '3':
                print(num1 * num2)
        elif escolha == '4':
                print(num1 / num2)
        elif escolha == '0':
                print('Saindo...')
                break
        else:
                print('Operação invalida. Tente novamente.')



