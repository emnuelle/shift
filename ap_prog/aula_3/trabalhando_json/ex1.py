# No slide nomeado como 'dicionario_para_json.py'
import json

contatos = {
    "Clark Kent":
        {"Celular":"123456",
        "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
        "Email":"bat@caverna.com.br"}
}

# Precisamos converter para json

dados_json = json.dumps(contatos, indent=4)

arquivo = open('agenda.json', 'w')
arquivo.write(dados_json)
arquivo.close()

