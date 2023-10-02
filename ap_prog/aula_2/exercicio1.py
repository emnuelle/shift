# Criando um calculadora com funções

def subtracao():
    print("Digite o primeiro numero:")
    numero1 = float(input())
    print("Digite o segundo numero:")
    numero2 = float(input())
    resultado = (numero1 - numero2)
    print(f"{numero1} - {numero2} = {resultado}")

def soma():
    print("Digite o primeiro numero:")
    numero1 = float(input())
    print("Digite o segundo numero:")
    numero2 = float(input())
    resultado = (numero1 + numero2)
    print(f"{numero1} + {numero2} = {resultado}")

def multiplicacao():
    print("Digite o primeiro numero:")
    numero1 = float(input())
    print("Digite o segundo numero:")
    numero2 = float(input())
    resultado = (numero1 * numero2)
    print(f"{numero1} * {numero2} = {resultado}")

def divisao():
    print("Digite o primeiro numero:")
    numero1 = float(input())
    print("Digite o segundo numero:")
    numero2 = float(input())
    resultado = (numero1 / numero2)
    print(f"{numero1} / {numero2} = {resultado}")

print("Escolha uma opção:")
print("(1) Subtração")
print("(2) Soma")
print("(3) Multiplicação")
print("(4) Divisão")

escolha = int(input())

if (escolha == 1):
    subtracao()
elif (escolha == 2):
    soma()
elif( escolha == 3):
    multiplicacao()
elif (escolha == 4):
    divisao()
else:
    print("Escolha uma opção válida!")


