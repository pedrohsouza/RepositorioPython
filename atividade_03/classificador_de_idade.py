idade = int(input("Informe a sua idade: "))

if idade <= 12:
    print(f"Você é uma criança")
elif idade > 12 and idade <= 17:
    print(f"Você é adolescente")
elif idade > 17 and idade <= 59:
    print(f"Você é adulto")
else:
    print(f"Você é idoso")
