import csv

# Nome do arquivo CSV
ARQUIVO = "pessoas.csv"


def ler_csv():
    """Lê um arquivo CSV e exibe os dados na tela."""
    try:
        with open(ARQUIVO, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            print("=== Dados das Pessoas ===")
            for linha in leitor:
                nome = linha["Nome"]
                idade = linha["Idade"]
                cidade = linha["Cidade"]
                print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO}' não encontrado.")
    except KeyError:
        print("Erro: o arquivo CSV deve conter as colunas 'Nome', 'Idade' e 'Cidade'.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


ler_csv()
