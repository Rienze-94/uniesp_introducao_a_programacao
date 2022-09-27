ano = int(input("Digite o ano atual:"))

dataNascimento = int(input("Digite o ano que você nasceu:"))

valor = ano - dataNascimento
print("Resultado:")

print (valor)

if valor >= 18:
    print ("Você esta apto a votar!")
else:
    print("Aguarde a maior idade!")
