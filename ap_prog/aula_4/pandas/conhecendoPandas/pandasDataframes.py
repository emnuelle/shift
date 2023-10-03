# O dataframe pode comportar dados de tipos diferentes, por isso uma das formas
#  mais interessantes de compormos essa estrutura é através de um dicionário!

import pandas as pd
import numpy as np

dataframe = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20210101"),
    "C": pd.Series([1.2, 3.7, 5.5, 6], dtype="float32"),
    "D": np.array([12,5,6,9], dtype="int32"),
    "E": pd.Categorical(["novo", "usado", "usado", "novo"])
})

print("Abaixo está nosso dataframe construído a partir de um dicionário")
print(dataframe)


