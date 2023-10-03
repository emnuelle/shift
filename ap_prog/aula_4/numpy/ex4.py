# No slide nomeado como ' ndarray04.py'

# Realizando operações com arrays ou entere eles
import numpy as np

array_inicial = np.array([[499.50, 25.00, 35.48], [350.15,30.12,17.3]])

array_resultado = array_inicial - 2
print("O ndarray resultado após a operação de subtração é")
print(array_resultado)

array_resultado = array_inicial * 2
print("O ndarray resultado após a operação de multiplicação é")
print(array_resultado)

array_resultado = array_inicial ** 2
print("O ndarray resultado após a operação de exponenciação é")
print(array_resultado)

array_resultado = array_inicial > 40
print("O ndarray resultado após a operação de comparação é")
print(array_resultado)


# Operações realizadas em dois ndarrays
array_a = np.array([[0,1], [2,0]])
array_b = np.array([[2,0], [4,3]])

array_resultado = array_a - array_b
print("O ndarray resultado após a operação de subtração é")
print(array_resultado)

array_resultado = array_a * array_b
print("O ndarray resultado após a operação de multiplicação dos elementos")
print(array_resultado)

array_resultado = array_a @ array_b
print("O ndarray resultado após a operação de multiplicação entre duas matrizes é")
print(array_resultado)


# Testando outras funções
array_a = np.array([[0,1], [2,0]])
print("A soma dos elementos do ndarray é")
print(array_a.sum())
print("O menor elemento do ndarray é")
print(array_a.min())
print("O maior elemento do ndarray é")
print(array_a.max())
print("A soma de cada coluna dos elementos do ndarray é")
print(array_a.sum(axis=0))