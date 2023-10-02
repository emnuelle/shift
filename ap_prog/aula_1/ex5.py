# No slide nomeado como 'if_composto.py'

print("Programa de gestão de doações\n")

print("Por favor, digite o valor da doação recebida!")
doacao = float(input())

if (doacao < 1000.00):
    investimento = doacao * 0.05
    uso_imediato = doacao - investimento
else:
    investimento =  doacao * 0.15
    uso_imediato = doacao - investimento

print(f"A doação de R${doacao:.2f} implica em um investimento de R${investimento:.2f},"
      f" restando R${uso_imediato:.2f} para uso imediato")

