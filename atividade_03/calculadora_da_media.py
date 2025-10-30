n1 = round(float(input("Informe a nota 1: ")), 1)
n2 = round(float(input("Informe a nota 2: ")), 1)
n3 = round(float(input("Informe a nota 3: ")), 1)
n4 = round(float(input("Informe a nota 4: ")), 1)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print(f"Média: {media:.1f}")


def resultadoExame():
    print("Aluno em exame.")
    nota_do_exame = round(float(input("Nota do exame: ")), 1)
    global media
    media = (media + nota_do_exame) / 2

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")


if media >= 7:
    print("Aluno aprovado.")
elif media >= 5 and media < 7:
    resultadoExame()
elif media < 5:
    print("Aluno reprovado.")

print(f"Media final: {media:.1f}")
