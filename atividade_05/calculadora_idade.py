from datetime import datetime


def calcularIdadeEmDias(ano_nascimento):
    ano_atual = datetime.now().year

    if ano_nascimento > ano_atual:
        return "O ano de nascimento não pode ser maior que o ano atual."

    idade_em_anos = ano_atual - ano_nascimento

    idade_em_dias = idade_em_anos * 365

    for ano in range(ano_nascimento, ano_atual + 1):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            idade_em_dias += 1

    return idade_em_dias


ano_nascimento = int(input("Digite seu ano de nascimento: "))
dias = calcularIdadeEmDias(ano_nascimento)
print(f"Sua idade em dias é: {dias} dias.")
