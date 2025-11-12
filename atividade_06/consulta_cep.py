import requests


def consultar_cep(cep):
    # Remove possíveis caracteres não numéricos
    cep = "".join(filter(str.isdigit, cep))

    # Monta a URL da API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"

    # Faz a requisição
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()

        # Verifica se o CEP é válido
        if "erro" in dados:
            print("❌ CEP não encontrado.")
        else:
            print("=== Resultado da Consulta ===")
            print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
            print(f"Bairro: {dados.get('bairro', 'Não informado')}")
            print(f"Cidade: {dados.get('localidade', 'Não informado')}")
            print(f"Estado: {dados.get('uf', 'Não informado')}")
    else:
        print("Erro ao consultar o CEP. Código de status:", resposta.status_code)


cep = input("Digite o CEP (apenas números): ")
consultar_cep(cep)
