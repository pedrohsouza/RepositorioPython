import requests


def consultar_cotacao(moeda):
    moeda = moeda.upper().strip()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()

        # A chave do dicionário é algo como 'USDBRL', 'EURBRL', etc.
        chave = f"{moeda}BRL"

        if chave in dados:
            cotacao = dados[chave]

            print("=== Cotação Atual ===")
            print(f"Moeda: {moeda}/BRL")
            print(f"Valor Atual: R$ {float(cotacao['bid']):.4f}")
            print(f"Máximo: R$ {float(cotacao['high']):.4f}")
            print(f"Mínimo: R$ {float(cotacao['low']):.4f}")
            print(f"Data e Hora da Última Atualização: {cotacao['create_date']}")
        else:
            print(
                "❌ Moeda não encontrada. Verifique o código informado (ex: USD, EUR, GBP)."
            )
    else:
        print("Erro ao acessar a API. Código de status:", resposta.status_code)


moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda)
