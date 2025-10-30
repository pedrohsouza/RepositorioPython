temperatura_inicial = float(input("Informe a temperatura: "))
unidade_origem = input("Informe a unidade de origem (C, K, F): ")
unidade_destino = input("Informe a unidade de destino (C, K, F): ")
temperatura_convertida = temperatura_inicial

print()


def conversorCelsius():
    if unidade_destino == "K":
        temperatura_convertida = temperatura_inicial + 273
        print(f"A temperatura em Kelvin é {temperatura_convertida} K ")
    elif unidade_destino == "F":
        temperatura_convertida = temperatura_inicial * 1.8 + 32
        print(f"A temperatura em Farenheit é {temperatura_convertida}°F ")


def conversorKelvin():
    if unidade_destino == "C":
        temperatura_convertida = temperatura_inicial - 273
        print(f"A temperatura em Celsius é {temperatura_convertida}°C ")
    elif unidade_destino == "F":
        temperatura_convertida = (temperatura_inicial - 273) * 1.8 + 32
        print(f"A temperatura em Farenheit é {temperatura_convertida}°F ")


def conversorFarenheit():
    if unidade_destino == "C":
        temperatura_convertida = (temperatura_inicial - 32) / 1.8
        print(f"A temperatura em Celsius é {temperatura_convertida}°C ")
    elif unidade_destino == "K":
        temperatura_convertida = (temperatura_inicial - 32) * (5 / 9) + 273
        print(f"A temperatura em Kelvin é {temperatura_convertida} K ")


if unidade_origem == "C":
    conversorCelsius()
elif unidade_origem == "K":
    conversorKelvin()
elif unidade_origem == "F":
    conversorFarenheit()
