def calcularGorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * porcentagem_gorjeta


valor_conta = round(float(input("Insira o valor da conta: ")), 2)
porcentagem_gorjeta = round(float(input("Insira a porcentagem da gorjeta: ")) / 100, 2)
gorjeta = calcularGorjeta(valor_conta, porcentagem_gorjeta)

print(f"Gorjeta: R$ {gorjeta:.2f}")
