# No slide nomeado como ' ndarray03.py'

import numpy as np

# nparray zerado // np.zeros((altura, largura))
array_zerado = np.zeros((3,4))
print("O array gerado com zeros ficou assim: ")
print(array_zerado)

# nparray "com 1"// np.zeros((altura, largura))
# dtype = data type
array_de_uns = np.ones((5,2), dtype=np.int32)
print("O array gerado com uns ficou assim: ")
print(array_de_uns)

# nparray com valores aleatórios
array_aleatorio = np.empty((6,3), dtype=np.int32)
print("O array gerado com valores aleatórios ficou assim: ")
print(array_aleatorio)

# nparray (parecido com a função range) // np.arange(parâmetro?)
#  A funçao '.reshape(linhas,colunas)'
array_gerado = np.arange(10).reshape(2,5)
print("O array gerado (com tipo range) ficou assim: ")
print(array_gerado)




