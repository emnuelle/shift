# construção do grafo
grafo = {}

grafo["inicial"] = {}
grafo["inicial"]["a"] = 8
grafo["inicial"]["b"] = 3

grafo["a"] = {}
grafo["a"]["final"] = 2

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["final"] = 2

grafo["final"] = {}

infinito = float("inf")  # representação de infinito em python
custos = {}
custos["inicial"] = 0
custos["a"] = infinito
custos["b"] = infinito
custos["final"] = infinito

pais = {}
pais["a"] = "inicial"
pais["b"] = "inicial"
pais["final"] = None

processados = []

# algoritmo
def achar_melhor_custo(custos):
    custo_baixo = float("inf")
    vertice_melhor_custo = None
    for vertice in custos:
        custo = custos[vertice]
        if custo < custo_baixo and vertice not in processados:
            custo_baixo = custo
            vertice_melhor_custo = vertice
    return vertice_melhor_custo

vertice = achar_melhor_custo(custos)
while vertice is not None:
    custo = custos[vertice]
    vizinhos = grafo[vertice]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = vertice
    processados.append(vertice)
    vertice = achar_melhor_custo(custos)

custo_minimo = custos["final"]
print("Custo mínimo:", custo_minimo)
