print("Sistema de votacao")
listaCandidatos = {}
resp = "s"
while (resp == "s"):
    candidato = input("Digite o nome do candidato")
    if candidato not in listaCandidatos.keys():
        listaCandidatos[candidato] = 1
    else:
        listaCandidatos[candidato]+=1
    resp = input("Deseja continuar (s/n)")

for c, v in listaCandidatos.items():
    print("O candidato ",c," teve ", v, " votos")