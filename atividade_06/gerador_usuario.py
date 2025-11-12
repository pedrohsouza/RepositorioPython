import requests


def gerarUsuario():
    # Faz a requisição para a API Random User Generator
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]

        # Extrai informações desejadas
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        # Exibe o resultado
        print("=== Perfil de Usuário Gerado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao gerar usuário. Código de status:", resposta.status_code)


gerarUsuario()
