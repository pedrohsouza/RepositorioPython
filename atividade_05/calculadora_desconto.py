preco_original = round(float(input("Informe o preço do produto: ")), 2)
porcentagem_desconto = round(float(input("Informe o percentual de desconto: ")), 2)

preco_final = preco_original - (preco_original * porcentagem_desconto) / 100

print(f"O preço final com desconto de {porcentagem_desconto}% é: R$ {preco_final:.2f}")
