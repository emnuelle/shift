#  Notas: A criação de uma nova série no pandas se dá através da instrução '.Series'
import pandas as pd
import numpy as np

serie = pd.Series([1,3,5,6,9])

print("Essa é uma estrutura de série no pandas")
print(serie)

# Também é possivel criar uma séries com um índice nomeado
indice = np.array(['A', 'B', 'C', 'D', 'E'])
serie = pd.Series([1, 3, 5, 6, 9], index=indice)

print("Essa é uma estrutura de série com um índice nomeado no pandas")
print(serie)



# Outro exemplo
# É possivél utilizar o método '.data_range()' para criar um intervalo de datas
indice_datas = pd.date_range("20200101", periods=6)

print("Abaixo está a estrutura que contém o índice das datas")
print(indice_datas)

# O método' empty 'do numpy está sendo usado para criar dados que irão ser simulados nos dataframes
array_aleatorio = np.empty((6,4), dtype=np.int32)
print("Abaixo está nosso array aleatorio que representa os dados do dataframe")
print(array_aleatorio)

# O 'dataframe' é composto dos dados do nosso array, tendo como índice das linhas as datas que foram geradas e as colunas e as letras A, B, C e D.
dataframe = pd.DataFrame(array_aleatorio, index=indice_datas, columns=['A', 'B', 'C', 'D'])
print("Abaixo está nosso dataframe")
print(dataframe)

