def lerNumero(mensagem):
    while True:
        entrada = input(mensagem).strip()
        try:
            if "." in entrada or "," in entrada:
                entrada = entrada.replace(",", ".")
                valor = float(entrada)
            else:
                valor = int(entrada)
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números (ex: 10 ou 3.14).")


def lerOperacao(mensagem):
    while True:
        entrada = input(mensagem).strip()
        if entrada == "+" or entrada == "-" or entrada == "*" or entrada == "/":
            return entrada
        else:
            print("❌ Entrada inválida! Digite apenas operações (ex: +, -, * ou /).")


def executarOperacao(numero_1, numero_2, operacao):
    resultado = 0
    try:
        if operacao == "+":
            resultado = numero_1 + numero_2
        elif operacao == "-":
            resultado = numero_1 - numero_2
        elif operacao == "*":
            resultado = numero_1 * numero_2
        elif operacao == "/":
            resultado = numero_1 / numero_2
    except ZeroDivisionError:
        print("❌ Operação inválida! Impossível dividir por zero.")
    return resultado


def exibirResultado(resultado):
    print(f"Resultado: {resultado}")


numero_1 = lerNumero("Insira o primeiro número: ")
numero_2 = lerNumero("Insira o segundo número: ")
operacao = lerOperacao("Insira a operação ( +, - , * ou /): ")
resultado = executarOperacao(numero_1, numero_2, operacao)
exibirResultado(resultado)
