from socket import *
from pickle import *
from datetime import *

ACK = 0
comando1 = "hi, meu nome eh"
comando2 = "bye"
comando3 = "list"
lista_nomes = []
lista_enderecos = []
ultimos_ack = []
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 4433))
print ("Servidor Pronto")
print("--------------------------------Iniciar Chat----------------------------------------")
def Atualizar_Acknowledge(numero_atual):
    if numero_atual == 0:
        return 1
    if numero_atual == 1:
        return 0
def Formatar_Horario(horario):
    separacao = horario.split(" ")
    data = separacao[0]
    hora = separacao[1]
    data_separada = data.split("-")
    hora_separada = hora.split(".")
    data_fomatada = f"{data_separada[2]}/{data_separada[1]}/{data_separada[0]}"
    hora_data = f"{hora_separada[0]} {data_fomatada}"
    return hora_data
while True:
    data, sender = serverSocket.recvfrom(1024)
    dado_desempacotado = load(data)
    mensagem = dado_desempacotado[1].decode()
    if sender in lista_enderecos:
        index_usuario = lista_enderecos.index(sender)
        
    if comando1 in mensagem and sender not in lista_enderecos:
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            lista_enderecos.append(sender)
            msg_dividida = mensagem.split(" ")
            lista_nomes.append(msg_dividida[4])
            ultimos_ack.append(dado_desempacotado[0])
            print(f"{mensagem[4]} entrou na sala")
        ################################################################################################
        respota = "Feito com sucesso"
        pacote_resposta = (dado_desempacotado[0], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            ultimos_ack[index_usuario] = Atualizar_Acknowledge(ultimos_ack[index_usuario])
        
    elif mensagem == comando2 and sender in lista_enderecos:
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            lista_enderecos.pop(index_usuario)
            print(f"{lista_nomes[index_usuario]} saiu da sala")
            lista_nomes.pop(index_usuario)
            ultimos_ack.pop(index_usuario)
        ################################################################################################
        respota = "Feito com sucesso"
        pacote_resposta = (dado_desempacotado[0], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            ultimos_ack[index_usuario] = Atualizar_Acknowledge(ultimos_ack[index_usuario])
        
    elif mensagem == comando3 and sender in lista_enderecos:
        resposta = lista_nomes.copy()
        ################################################################################################
        pacote_resposta = (dado_desempacotado[0], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            ultimos_ack[index_usuario] = Atualizar_Acknowledge(ultimos_ack[index_usuario])
            
    elif sender in lista_enderecos:
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            horario = datetime.now()
            horario_formatado = Formatar_Horario(str(horario))
            print(f"{sender[0]}:{sender[1]}/~{lista_nomes[index_usuario]}: {mensagem} {horario_formatado}")
        ################################################################################################
        respota = "Feito com sucesso"
        pacote_resposta = (dado_desempacotado[0], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)
        if dado_desempacotado[0] != ultimos_ack[index_usuario]:
            ultimos_ack[index_usuario] = Atualizar_Acknowledge(ultimos_ack[index_usuario])
    
    else:
        resposta = "Conecte-se ao chat usando o comando (hi, meu nome eh <nome_do_usuario>)"
        pacote_resposta = (dado_desempacotado[0], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)