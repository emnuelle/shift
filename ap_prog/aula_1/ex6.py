# No slide nomeado como 'if_encadeado.py'

print("Descubra se você pode utilizar o nosso transporte:")
print("Digite sua idade:")
idade = int(input())

if (idade <= 16):
    print("De acordo com a a legislação você ainda não pode votar,"
          " o que impossibilita o uso do nosso transporte.")
elif (idade <= 18):
    print("Acesso liberado! Lembrando que com a sua "
          "idade você ainda pode optar por votar ou não")
else:
    print("Acesso liberado! O voto é obrigatório.")
