servicos = {'revisao':300,'motor':1000}


pecas    = {'filtro de oleo':100, 'oleo':200,'pastilha':800,'filtro':200}

def precoTotal(texto):
    linha = texto[8:]
    lista = linha.split(';')
    servico = lista[0]
    print("O servico pedido foi:",servico)
    preco = servicos[servico]
  ##  for i in range(1:len(lista))
    for l in lista:
        if l in pecas.keys():
            preco += pecas[l]
    return preco

print("Sistema de manutencao de veiculos")
total = precoTotal("GHQ2303 revisao;oleo;filtro")
print("total = ",total)
