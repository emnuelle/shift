
# Abrindo a bomba
arquivo = open('D:/pythonJourney_machineLearning_shift'
               '/appliedProgramming/aula_4/arquivos_txt'
               '/arquivo.txt')
print(arquivo.readline())

arquivo.close()


# Escrevendo
conteudo = "ai que meiga uma fofa"
arquivo = open('arquivo.txt', 'w')
arquivo.write(conteudo)
arquivo.close()
