# 1) Desenvolva uma função para calcular a série Fibonacci
# de uma quantidade de termos fornecidos pelo usuário.

def fibonacci(termo):
    if termo == 1:
        return 0
    elif termo == 2:
        return 1
    else:
        return fibonacci(termo - 1) + fibonacci(termo - 2)

termo = 5
for i in range(1, termo + 1):
    print(fibonacci(i))
    
# 2) Desenvolva uma função utilizando a recursividade para
# calcular o valor fatorial de um numero inteiro.


# 3) Desenvolva uma função que recebe um número e verifica
# se esse valor é igual a 1. Se for, deve retornar 1, afinal:
# soma(1) = 1. Entretanto, se não for 1, deve retornar: n +
# soma(n-1)