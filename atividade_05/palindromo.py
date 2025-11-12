def verificarPalindromo(mensagem):
    entrada = input(mensagem).strip().lower()
    tamanho_entrada = len(entrada)

    for i in range(tamanho_entrada):
        if entrada[i] != entrada[tamanho_entrada - i - 1]:
            return "Não"
    return "Sim"


resultado = verificarPalindromo("Insira a palavra: ")
print(resultado)
