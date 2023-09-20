lista_nomes = ["joao", "pedro", "roberto"]
lista_enderecos = [("444", 1232),("555", 2351),("44764", 8598)]
resposta = ""

for nome, endereco in zip(lista_nomes, lista_enderecos):
    resposta = resposta + nome + "/" + str(endereco[0]) + ":" + str(endereco[1]) + " "

print(resposta)