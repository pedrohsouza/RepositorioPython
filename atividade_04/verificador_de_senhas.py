def senhaForte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True


while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == "sair":
        print("Encerrando o programa.")
        break

    if senhaForte(senha):
        print("Senha forte! ✅")
        break
    else:
        print(
            "Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.\n"
        )
