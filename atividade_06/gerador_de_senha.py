import random

caracteres_especiais = "!@#$%¨&*()_+[]?/;.,"
caracteres = "qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM1234567890"
quantidade_de_caracteres = int(input("Informe a quantidade de caracteres da senha: "))
senha = ""

for caractere in range(quantidade_de_caracteres):
    lista_selecionada = random.randint(1, 2)

    if lista_selecionada == 1:
        caractere_selecionado = random.randint(0, len(caracteres_especiais) - 1)
        senha = senha + caracteres_especiais[caractere_selecionado]
        continue

    caractere_selecionado = random.randint(0, len(caracteres) - 1)
    senha = senha + caracteres[caractere_selecionado]

print(f"Senha: {senha}")
