import numpy as np

novo_array = np.array([1,2,3])

print("Abaixo está o seu Array: ")
print(novo_array)

# .ndim para retornar a quantidade de dimensões (eixos)
print(f"Esse é o um ndarray com {novo_array.ndim} dimensões")
# .shape para retornar as dimenções do array (Uma tupla contendo o tamnho de cada dimensão)
print(f"As dimensões desse ndarray possuem os seguintes tamanhos: {novo_array.shape}")
# .size para retornar a quantidade de elementos presentes no array
print(f"Ao todo, esse ndarray contém {novo_array.size} elementos")
# .dtype para retornar o tipo dos elementos presentes dentro do array
print(f"Os elementos presentes esse ndarray são do tipo {novo_array.dtype}")
# .itemsize para retornar o tamanho em bytes dos elementos do array
print(f"Os elementos presentes nesse ndarray ocupam {novo_array.itemsize} bytes")

