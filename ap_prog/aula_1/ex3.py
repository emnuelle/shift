# No slide como 'calculadora.py'

print("Programa de calculadora")

print("Por favor, digite o primeiro valor:")
valor1 = float(input())
print("Por favor, digite o segundo valor:")
valor2 = float(input())

soma = valor1 + valor2
subtracao = valor1 - valor2
divisao = valor1 / valor2
multiplicacao = valor1 * valor2

print(f"{valor1}+{valor2}={soma}")
print(f"{valor1}-{valor2}={subtracao}")
print(f"{valor1}/{valor2}={divisao}")
print(f"{valor1}*{valor2}={multiplicacao}")
