print ("[!]Promoção[!]")
print ("maçãs por 1,30r$ ou acima de 12 por apenas 1,00r$ !")

maçãs = int(input("digite quantas maçãs quer comprar:"))

preçoPromoção = 1.00
preçocomum = 1.30

valorPromoção = maçãs * preçoPromoção
valorComum = maçãs * preçocomum

print ("VALOR A PAGAR:")
if maçãs >=12:
    print (valorPromoção)
elif maçãs <= 11:
        print (ValorComum)