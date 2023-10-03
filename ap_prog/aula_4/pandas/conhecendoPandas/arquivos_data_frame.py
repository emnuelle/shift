# Explorando operações de importação e exportação de dados com o Pandas
import pandas as pd
import numpy as np

dataframe = pd.DataFrame({
"A": 1.0,
"B": pd.Timestamp("20210101"),
"C": pd.Series([1.2, 3.7, 5.5, 6], dtype="float32"),
"D": np.array([12,5,6,9], dtype="int32"),
"E": pd.Categorical(["novo", "usado", "usado", "novo"])
})


# É possivel exportar um data frame para o formato csv
print("Exportando dataframe para o formato CSV")
dataframe.to_csv("arquivo_csv.csv")

#  Também podemos exportar para o formato Exel. Para isso o pacote 'openpyxl' deve estar instalado // 'pip install openpyxl' no cmd 
print("Exportando dataframe para o formato XLSX")
dataframe.to_excel("arquivo_excel.xlsx", sheet_name="Sheet1")

#  A conversão para o formato JSON também é possivel
print("Convertendo o dataframe para o formato JSON")
print(dataframe.to_json())


# A abertura de arquivos para o formato datafram é simples igual
# Para csv
dataframe = pd.read_csv("arquivo_csv.csv")
print("Aqui está o dataframe recuperado do arquivo CSV")
print(dataframe)

# Para excel
dataframe = pd.read_excel("arquivo_excel.xlsx")
print("Aqui está o dataframe recuperado do arquivo XLSX")
print(dataframe)