
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    while True:
        print("\nCalculadora Simples")
        print("Escolha a operação:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("0 - Sair")

        escolha = input("Digite o número da operação (0 a 4): ")

        if escolha == '0':
            print("Encerrando a calculadora. Até logo!")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: entrada inválida. Digite apenas números.")
                continue

            if escolha == '1':
                print("Resultado:", somar(num1, num2))
            elif escolha == '2':
                print("Resultado:", subtrair(num1, num2))
            elif escolha == '3':
                print("Resultado:", multiplicar(num1, num2))
            elif escolha == '4':
                print("Resultado:", dividir(num1, num2))
        else:
            print("Operação inválida. Tente novamente.")

# Executar a calculadora
calculadora()
