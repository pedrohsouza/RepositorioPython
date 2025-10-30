peso = float(input("Informe o peso: "))
altura = float(input("Informe a altura: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"IMC: {imc}, classificação = abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"IMC: {imc}, classificação = peso normal")
elif imc >= 25 and imc < 30:
    print(f"IMC: {imc}, classificação = sobrepeso")
else:
    print(f"IMC: {imc}, classificação = obeso")
