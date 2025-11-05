def lerNotas(mensagem):
    notas = []
    while True:
        entrada = input(mensagem).strip()
        try:
            if entrada == "fim":
                if len(notas) > 0:
                    break
                print("❌ Insira ao menos uma nota")
                continue
            elif "." in entrada or "," in entrada:
                entrada = entrada.replace(",", ".")
                nota = float(entrada)
            else:
                nota = int(entrada)

            if nota >= 0 and nota <= 10:
                notas.append(nota)
            else:
                print("❌ Entrada inválida! Digite apenas valores de 0 a 10.")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números (ex: 10 ou 3.14).")
    return notas


def calcularMedia(notas):
    soma_das_notas = 0

    for nota in notas:
        soma_das_notas = soma_das_notas + nota

    return soma_das_notas / len(notas)


def exibirMedia(media):
    print(f"Média da turma: {media:.2f}")


notas = lerNotas("Insira uma nota: ")
media = calcularMedia(notas)
exibirMedia(media)
