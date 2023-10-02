# No slide nomeado como 'tabuada_for.py'

print("Digite o número do qual deseja obter a tabuada:")
numero = int(input())

for multiplicador in range(1, 11, 1):
    resultado = multiplicador * numero
    print(f"{multiplicador} x {numero} = {resultado}")
