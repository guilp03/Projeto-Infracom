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
ultimo_seq = []

# Funcoes auxiliares

def Atualizar_Operador(numero_atual):
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
    data_fomatada = f"{data_separada[2]}/{data_separada[1]}/{data_separada[0]}" # converte a data para o formato Dia/Mes/Ano
    hora_data = f"{hora_separada[0]} {data_fomatada}"
    return hora_data

def retransmitir_pacote(seq, msg, destino):
    pacote = (0,seq,msg.encode())
    pacote_serializado = dumps(pacote)
    serverSocket.sendto(pacote_serializado, destino)
    return

# Definicao do Socket do server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 4433))
# Print inicial para mostrar que o server esta disponivel e o chat foi iniciado
print ("Servidor Pronto")
print("--------------------------------Iniciar Chat--------------------------------")

# Loop infinito que garante que o server esteja sempre em execução
while True:
    while True:
        try:
            serverSocket.settimeout(1)
            data, sender = serverSocket.recvfrom(1024)
            break
        except timeout:
            continue
    dado_desempacotado = loads(data)
    mensagem = dado_desempacotado[2].decode()
    if sender in lista_enderecos:
        index_usuario = lista_enderecos.index(sender)
    #REPETICAO DESNECESSARIA
    if sender in lista_enderecos and dado_desempacotado[1] != ultimos_ack[index_usuario]:
        pacote_resposta = (1,ultimos_ack[index_usuario], "ack".encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
    
    #COMANDO 1 = 'hi, meu nome eh' 
    elif comando1 in mensagem and sender not in lista_enderecos:
        lista_enderecos.append(sender)
        msg_dividida = mensagem.split(" ")
        lista_nomes.append(msg_dividida[4])
        ultimos_ack.append(dado_desempacotado[1])
        ultimo_seq.append(0)
        index_usuario = lista_enderecos.index(sender)
        resposta = (f"{msg_dividida[4]} entrou na sala")
        ################################################################################################
        for i in range (len(lista_nomes)):
            if lista_enderecos[i] != sender:
                pacote_resposta = (0,ultimo_seq[i], resposta.encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                while True:
                    serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                    try:
                        serverSocket.settimeout(5.0)
                        ack, emissor = serverSocket.recvfrom(1024)
                        ack_unpacket = loads(ack)
                        if emissor == lista_enderecos[i] and ack_unpacket[1] == ultimo_seq[i]:
                            ultimo_seq[i] = Atualizar_Operador(ultimo_seq[i])
                            break
                    except timeout:
                        continue
            else:
                pacote_resposta = (1,ultimos_ack[i], resposta.encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                ultimos_ack[i] = Atualizar_Operador(ultimos_ack[i])
                
    #COMANDO 2 = 'bye'
    elif mensagem == comando2 and sender in lista_enderecos:
        resposta = (f"{lista_nomes[index_usuario]} saiu da sala")
        ################################################################
        for i in range (len(lista_nomes)):
            if lista_enderecos[i] != sender:
                pacote_resposta = (0,ultimo_seq[i], resposta.encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                while True:
                    serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                    try:
                        serverSocket.settimeout(5.0)
                        ack, emissor = serverSocket.recvfrom(1024)
                        ack_unpacket = loads(ack)
                        if emissor == lista_enderecos[i] and ack_unpacket[1] == ultimo_seq[i]:
                            ultimo_seq[i] = Atualizar_Operador(ultimo_seq[i])
                            break
                    except timeout:
                        continue
            else:
                pacote_resposta = (1,ultimos_ack[i], "ack".encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                ultimos_ack[i] = Atualizar_Operador(ultimos_ack[i])
        lista_enderecos.pop(index_usuario)
        lista_nomes.pop(index_usuario)
        ultimos_ack.pop(index_usuario)
        ultimo_seq.pop(index_usuario)
        
    #COMANDO 3 = 'list'
    elif mensagem == comando3 and sender in lista_enderecos:
        resposta = ""
        for nome, endereco in zip(lista_nomes, lista_enderecos):
            resposta = resposta + nome + "/" + str(endereco[0]) + ":" + str(endereco[1]) + " "
        ################################################################################################
        pacote_resposta = (0,ultimo_seq[index_usuario], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        while True:
            serverSocket.sendto(pacote_resposta_serializado, sender)
            try:
                serverSocket.settimeout(5.0)
                ack, emissor = serverSocket.recvfrom(1024)
                ack_unpacket = loads(ack)
                if emissor == sender and ack_unpacket[1] == ultimo_seq[index_usuario]:
                    ultimo_seq[index_usuario] = Atualizar_Operador(ultimo_seq[index_usuario])
                    break
            except timeout:
                continue
            
    #MENSAGEM QUALQUER
    elif sender in lista_enderecos:
        horario = datetime.now()
        horario_formatado = Formatar_Horario(str(horario))
        ################################################################################################
        resposta = (f"{sender[0]}:{sender[1]}/~{lista_nomes[index_usuario]}: {mensagem} {horario_formatado}")
        for i in range (len(lista_nomes)):
            if lista_enderecos[i] != sender:
                pacote_resposta = (0,ultimo_seq[i], resposta.encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                while True:
                    serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                    try:
                        serverSocket.settimeout(5.0)
                        ack, emissor = serverSocket.recvfrom(1024)
                        ack_unpacket = loads(ack)
                        if emissor == lista_enderecos[i] and ack_unpacket[1] == ultimo_seq[i]:
                            ultimo_seq[i] = Atualizar_Operador(ultimo_seq[i])
                            break
                    except timeout:
                        continue
            else:
                pacote_resposta = (1,ultimos_ack[i], "ack".encode())
                pacote_resposta_serializado = dumps(pacote_resposta)
                serverSocket.sendto(pacote_resposta_serializado, lista_enderecos[i])
                ultimos_ack[i] = Atualizar_Operador(ultimos_ack[i])
    
    else:
        resposta = "Conecte-se ao chat usando o comando (hi, meu nome eh <nome_do_usuario>)"
        pacote_resposta = (1, dado_desempacotado[1], resposta.encode())
        pacote_resposta_serializado = dumps(pacote_resposta)
        serverSocket.sendto(pacote_resposta_serializado, sender)