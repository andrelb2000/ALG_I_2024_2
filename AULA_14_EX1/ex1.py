
arquivo = open("defeitos.txt","r")
todasLinhas = arquivo.readlines()
totalfalha = 0
for linha in todasLinhas:
    codPeca = linha[:4]
    data    = linha[5:14]
    listaX = linha[15:].split(",")
    print("Peca:",codPeca, " falhou ", len(listaX), " vezes")
    totalfalha += len(listaX)
print("Total de falhas ", totalfalha)