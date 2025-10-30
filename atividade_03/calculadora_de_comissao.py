nome_vendedor = input("Informe o nome do vendedor: ")
salario_fixo = round(float(input("Informe o salário fixo (R$): ")), 2)
total_de_vendas = round(float(input("Informe o total de vendas (R$): ")), 2)

salario = salario_fixo + total_de_vendas * 0.15

print(f"O salário total a ser recebido é de R$ {salario:.2f}")
