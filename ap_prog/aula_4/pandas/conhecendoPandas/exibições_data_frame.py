# Explorando operações com dataframes

import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
{
"A": 1.0,
"B": pd.Timestamp("20210101"),
"C": pd.Series([1.2, 3.7, 5.5, 6], dtype="float32"),
"D": np.array([12,5,6,9], dtype="int32"),
"E": pd.Categorical(["novo", "usado", "usado", "novo"])
}
)

# Printando o normal aqui pra facilitar no entendimento
print()
print("Aqui está o dataframe completo: ")
print(dataframe)
print()

#  Podemos exibir os dados de uma coluna específica, inidicando entre colchetes o valor dessa coluna
print("Abaixo exibimos os dados da coluna C")
print(dataframe["C"])

# Um intervalo de linhas pode ser especificado, indicando primeiro a partir de que linha o corte deve ser feito seguido da quantidade de linhas. Nesse caso serão exibidas as duas primeiras
print("Abaixo exibimos apenas um intervalo de linhas")
print(dataframe[0:2])

# É possivél fazer a exibição dos dados baseado em uma operação booleana. Nesse caso só serão exibidas linhas onde a coluna D tenha calores maiores do que 7
print("Abaixo exibimos apenas os valores do dataframe em que a coluna D seja maior do que 7")
print(dataframe[dataframe["D"] > 7])

# Também é possivél exibir apenas as linhas que contenham valores em um determinado intervalo, através do método '.isi()'. No caso só seram exibidas linhas em que a coluna 'E' contém o valor "Usado"
print("Abaixo exibimos apenas os valores em que a coluna E contém o valor 'usado'")
print(dataframe[dataframe["E"].isin(["usado"])])
