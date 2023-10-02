# No slide nomeado como 'dicionario_ex01.py'

notas = {}
encerrar = "NÃO"

while "N" in encerrar.upper():
    print("Por favor, digite o nome do aluno:")
    aluno = input()
    print("Por favor, digite a nota do aluno:")
    nota = float(input())

    print("Deseja FINALIZAR a digitação?\n(S)\tSim\n(N)\tNão")
    encerrar = input()

total = 0
for nota in notas.values():
    if nota == 10.00:
        total = total + 1

print(f"Ao total, {total} alunos tiraram notas 10!")

print("Notas da turma: ")
for aluno, nota in notas.items():
    print(f"O aluno {aluno} tirou nota {nota}.")
