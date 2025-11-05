def lerNumero(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            if entrada == "fim":
                return entrada
            else:
                valor = int(entrada)
                return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números inteiros (ex: 5 ou 8).")


total_pares = 0
total_impares = 0

while True:
    numero = lerNumero("Insira um número inteiro: ")
    if numero == "fim":
        break
    elif numero % 2 == 0:
        total_pares = total_pares + 1
        print("O número é par")
    else:
        total_impares = total_impares + 1
        print("O número é ímpar")

print(f"Total de números pares: {total_pares}")
print(f"Total de números ímpares: {total_impares}")
