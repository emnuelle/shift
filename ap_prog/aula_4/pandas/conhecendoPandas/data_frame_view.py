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

# O método '.head()' exibe os elementos da parte de cima do dataframe
print("Abaixo está a parte de cima do nosso dataframe")
print(dataframe.head())

# O método '.tail()' exibe os elemtnos da parte de baixo do dataframe
print("Abaixo está a parte de baixo do nosso dataframe")
print(dataframe.tail(2))

# O atributo '.index' exibe os índices da parte do dataframe
print("Abaixo estão os índices do nosso dataframe")
print(dataframe.index)

# O atributo '.columns' exobe as colunas da parte do dataframe
print("Abaixo estão as colunas do nosso dataframe")
print(dataframe.columns)

# O método 'to_numpy()' retorno os elementos do dataframe com um ndarray
print("Abaixo está nosso dataframe convertido para um array numpy")
print(dataframe.to_numpy())

# O método '.describe()' realiza operações de estatística básica 
print("Abaixo estão estatísticas básicas dobre nosso dataframe")
print(dataframe.describe())

# O método '.sort_values(by="(Coluna)")' odena os dados de uma coluna
print("Abaixo está nosso dataframe ordenado por uma coluna")
print(dataframe.sort_values(by="D"))
