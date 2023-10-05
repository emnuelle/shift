def penquisa_binaria(lista, num):
    baixo = 0
    alto = len(lista)-1

    while baixo <= alto:
        meio = (baixo+alto) // 2
        chute = lista[meio]
        if chute == num:
            return meio
        if chute > num:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

lista = [1,3,5,7,9,11,13,15]

#retorna o índice do vetor
print(penquisa_binaria(lista, 5))
print(penquisa_binaria(lista, 15))
