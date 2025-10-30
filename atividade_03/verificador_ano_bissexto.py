ano = int(input("Informe o ano: "))
print()

if ano % 100 == 0:
    if ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")
elif ano % 4 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
