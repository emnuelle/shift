from collections import deque

grafo = {}

grafo["maria"] = ["joão", "miriam", "jose"]
grafo["joão"] = ["paulo", "pedro"]
grafo["jose"] = ["miriam"]
grafo["miriam"] = ['elias']
grafo["paulo"] = []
grafo["pedro"] = []
grafo["elias"] = []


def pesquisa(nome):
    fila = deque()
    fila += grafo[nome]
    verificadas = []
    while fila:
        pessoa = fila.popleft()
        if not pessoa in verificadas:
            if pescador(pessoa):
                print(pessoa + " é pescador")
            else:
                fila += grafo[pessoa]
                verificados.append(pessoa)
    print("NMão existem pescadores")
    return False

def pescador(nome):
    return nome[-1] == 's'

pesquisa("jose")

