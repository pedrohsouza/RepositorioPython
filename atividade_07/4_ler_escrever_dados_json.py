import json

# Nome do arquivo JSON
ARQUIVO = "pessoa.json"


def salvar_pessoa(nome, idade, cidade):
    """Salva as informações da pessoa em um arquivo JSON."""
    pessoa = {"nome": nome, "idade": idade, "cidade": cidade}

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    print(f"Dados salvos em '{ARQUIVO}' com sucesso!")


def ler_pessoa():
    """Lê as informações da pessoa do arquivo JSON."""
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            pessoa = json.load(arquivo)
            print("Dados da pessoa:")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")
            print(f"Cidade: {pessoa['cidade']}")
    except FileNotFoundError:
        print(f"Arquivo '{ARQUIVO}' não encontrado. Salve uma pessoa primeiro.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique o formato do arquivo.")


def main():
    print("=== Cadastro de Pessoa ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cidade = input("Cidade: ")

    salvar_pessoa(nome, idade, cidade)
    print("\nLendo dados do arquivo...\n")
    ler_pessoa()


main()
