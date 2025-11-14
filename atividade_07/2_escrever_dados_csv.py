import csv

# Dados que queremos escrever no arquivo CSV
dados_pessoais = [
    {"Nome": "João", "Idade": 28, "Cidade": "São Paulo"},
    {"Nome": "Maria", "Idade": 22, "Cidade": "Rio de Janeiro"},
    {"Nome": "Carlos", "Idade": 35, "Cidade": "Belo Horizonte"},
    {"Nome": "Ana", "Idade": 30, "Cidade": "Curitiba"},
]

# Nome do arquivo CSV
nome_arquivo = "dados_pessoais.csv"

# Criar e escrever no arquivo CSV
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    # Definir os nomes das colunas
    campos = ["Nome", "Idade", "Cidade"]

    # Criar um objeto writer
    writer = csv.DictWriter(arquivo_csv, fieldnames=campos)

    # Escrever o cabeçalho
    writer.writeheader()

    # Escrever os dados
    for dado in dados_pessoais:
        writer.writerow(dado)

print(f"Os dados foram escritos no arquivo {nome_arquivo}.")
