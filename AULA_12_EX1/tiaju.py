
sobrinhos = {}

## Criar função que recebe nome e idade e coloca no dicionario
def inserirSobrinho(dicionario,nome,idade):
    ## O dicionario insere o nome do sobrinho e a idade e o 
    # dinheiro em uma listinha
    dicionario[nome] = [idade,0.0]

def distribuirMesada(dicionario,total):
    somaIdades = 0
    for item in dicionario.values():
        somaIdades += item[0]
    for item in dicionario.values():
        item[1] = total * item[0] /somaIdades

## Retorna o nome do sobrinho que tem mais grana ##
def maisGrana(dicionario):
    maior = 0
    maisRico = ""
    for (chave,listinha) in dicionario.items():
        if (listinha[1] > maior): 
            maior = listinha[1]
            maisRico = chave

    return (maisRico)

       


# Programa principal
inserirSobrinho(sobrinhos,"Murilo",16)
inserirSobrinho(sobrinhos,"Rafael",43)
inserirSobrinho(sobrinhos,"Braga",35)
inserirSobrinho(sobrinhos,"Savio",57)

distribuirMesada(sobrinhos,500)


print(sobrinhos)

print("o mais rico é o ",maisGrana(sobrinhos))