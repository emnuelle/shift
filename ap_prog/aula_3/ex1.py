# No slide nomeado como 'listas_ex01.py'

notas = []
encerrar = "NÃO"

while "N" in encerrar.upper() :
    print("Por favor, digite uma nova nota:")
    nova_nota = float(input())
    notas.append(nova_nota)

    print("Deseja FINALIZAR a digitação?\n(S)\tSim\n(N)\tNão")
    encerrar = input()

print(f"Ao total, {notas.count(10)} alunos tiraram nota 10!")

notas.sort()
notas.reverse()

print("Notas da turmas:")
for nota in notas:
    print(nota)