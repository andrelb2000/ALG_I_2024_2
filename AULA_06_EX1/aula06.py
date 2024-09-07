preco = 0.0
maiorPreco = 0.0
menorPreco = 100000000.0
continuar = 'S'
lista = []
## for i in range(3):
while(continuar == 'S'):
    preco = float(input("Entre com o preço: "))
    lista.append(preco)
    if(preco > maiorPreco):
        maiorPreco = preco
    if(preco < menorPreco):
        menorPreco = preco
    print("O preco digitado foi: ",preco)
    continuar = input("Deseja inserir mais um ?")
print("O maior preco foi: ",maiorPreco)
print("O menor preco foi: ",menorPreco)
###print("Lista = ",lista)
for elemento in lista:
    print("Preco digitado R$ ",elemento)
