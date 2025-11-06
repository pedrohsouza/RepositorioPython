nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

preco_final = preco_original - (preco_original * porcentagem_desconto) / 100

print(f"Nome do produto: {nome_do_produto}")
print(f"Preço original: R$ {preco_original}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"O preço final com desconto de {porcentagem_desconto}% é: R$ {preco_final:.2f}")
