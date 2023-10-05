
# Implementação de inserção direta
import random 

def insercao_direta(vetor):
    n = len(vetor)
    for j in range(1,n):
        temp = vetor [j]
        i = j - 1
        while i >= 0 and vetor[i] > temp:
            vetor[i+1] = vetor[i]
            i = i - 1
        vetor[i+1] = temp
        
# Para criarmos uma lista com 20 valores aleatórios entre 1 e 100
lista = random.sample(range(1, 100), 20)

print("Lista não ordenada:", lista)
insercao_direta(lista)
print("Lista ordenada:", lista)


# Implementaçãoo de Shell Sort
def shell_sort(veotr, n):
    intervalo = n // 2
    while intervalo > 0:
        for i in range(intervalo, n):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
                vetor[j] = temp
                intervalo = intervalo // 2
                
# Testando criando uma lista com 20 valores aleatórios entre 1 e 100
lista = random.sample(range(1,100),20)

print("Lista não ordenada: ", lista)
shell_sort(lista, len(lista))
print("Lista ordenada:", lista)


# Implementaçãoo de bubble Sort
def bubble_sort(vetor):
    for i in range(len(vetor), 0, -1):
        troca = False
        for j in range(0, i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j + 1], vetor[j] = vetor[j], vetor[j + 1]
                troca = True
            if not troca:
             break
         
#  lista com 20 valores aleatórios entre 1 e 100
lista = random.sample(range(1, 100), 20)

print("Lista não ordenada: ", lista)
bubble_sort(lista)
print("Lista ordenada:", lista)



# Recursividade: é a forma de resolver problemas dividindo-o em partes menores, quando uma função chama ela mesma para resolver um problema.
# EX. função para somar uam sequência numérica

# com FOR
def soma1(n):
    soma = 0 
    for i in range(n+1):
        sama += i
    return soma

# Com recusividade 
def soma2(n):
    if n == 0:
        return 0 
    return n + soma2(n-1)


  
     
