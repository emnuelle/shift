
class item():
    def __ninit__(self, nome, valor, peso):
        self.nome = nome
        self.valor = valor
        self.peso = peso
        
class Individuo():
    def __init__(self, pesos, valores):
        self.pesos = pesos
        self.valores = valores
        self.limite_peso = 10
        self.nota_avaliacao = 0
        self.geracao = 0
        self.cromossomo = []
        self.avialiacao = 0
        for i in range(len(pesos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
                
if __name__ == "__main__":
    lista_itens = []
    lista_itens.append(Item("Lanterna", 80, 1))
    lista_itens.append(Item("Faca", 85, 1))
    lista_itens.append(Item("Roupas", 90, 3))
    lista_itens.append(Item("Livros", 50, 0.5))
    lista_itens.append(Item("Saco de dormir", 105, 2))
    lista_itens.append(Item("Remédios", 90, 2))
    lista_itens.append(Item("Alimentos", 200, 4))
    lista_itens.append(Item("Rede de descanso", 100, 2.5))
    
valores = []
pesos = []

for item in lista_itens:
    valores.append(item.valor)
    pesos.append(item.peso)
    
individuo_1 = Individuo(pesos, valores)
print("Pesos = %s" % str(individuo_1.pesos))
print("Valores = %s" % str(individuo_1.valores))
print("Cromossomo = %s" % str(individuo_1.cromossomo))

def fitness(self):
    nota = 0
    soma_pesos = 0
    for i in range(len(self.cromossomo)):
        if self.cromossomo[i] == '1':
            nota += self.valores[i]
            soma_pesos += self.pesos[i]
    if soma_pesos > self.limite_peso:
        nota = 1
        self.avaliacao = nota
        self.peso_total = soma_pesos

individuo_1 = Individuo(pesos, valores)
print("Indivíduo 1")
print("Pesos = %s" % str(individuo_1.pesos))
print("Valores = %s" % str(individuo_1.valores))
print("Cromossomo = %s" %
str(individuo_1.cromossomo))

individuo_1.fitness()
print("Avaliação = %s " % individuo_1.avaliacao)
print("Peso total: = %s " %
individuo_1.peso_total)

Individuo_1 = Individuo(pesos, valores)
print("Indivíduo 1")
print("Pesos = %s" % str(individuo_1.pesos))
print("Valores = %s" %
str(individuo_1.valores))
print("Cromossomo = %s" %
str(individuo_1.cromossomo))
individuo_1.fitness()
print("Avaliação = %s " %
individuo_1.avaliacao)
print("Peso total: = %s " %
individuo_1.peso_total)
print("----------------")

Individuo_2 = Individuo(pesos, valores)
print("Indivíduo 2")
print("Pesos = %s" % str(individuo_2.pesos))
print("Valores = %s" % str(individuo_2.valores))
print("Cromossomo = %s" %
str(individuo_2.cromossomo))
individuo_2.fitness()
print("Avaliação = %s " % individuo_2.avaliacao)
print("Peso total = %s " %
individuo_2.peso_total)
filhos = individuo_1.crossover(individuo_2)
print("Filho 1 = %s" % filhos[0].cromossomo)
print("Filho 2 = %s" %filhos[1].cromossomo)