from socket import *
from pickle import *
import threading
import time

SEQ = 0
ACK = 1
recebido = False
def retransmitir_pacote(seq, msg):
    pacote = (1,seq,msg.encode())
    pacote_serializado = dumps(pacote)
    client.sendto(pacote_serializado, server_adress)
    return
temporizador = threading.Timer(1.0, retransmitir_pacote, args= SEQ)

server_adress = ("127.0.0.1", 4433)
client = socket(AF_INET, SOCK_DGRAM)

def Send(server_adress):
    global SEQ
    global ACK
    global temporizador
    
    while True:
        msg = input("-> ")
        pacote = (SEQ, msg.encode())
        pacote_serializado = dumps(pacote)
        client.sendto(pacote_serializado, server_adress)
        temporizador = threading.Timer(1.0, retransmitir_pacote, args= (SEQ, msg))
        while recebido == False:
            temporizador.start() 
    return
def receive():
    global SEQ
    global ACK
    global temporizador
    while True:
        mensagem, sender = client.recvfrom(1024)
        data = loads(mensagem)
        if data[0] == 1:
            if data[1] == SEQ:
                temporizador.cancel()
                recebido = True
                if SEQ == 1:
                    SEQ = 0
                else:
                    SEQ = 1
        elif data[0] == 0:
            if data[1] != ACK:
                print(data[2].decode())
                sendack(data[1])
                if ACK == 1:
                    ACK = 0
                else:
                    ACK = 1
            else:
                sendack(data[1])
        
def sendack(ack):
    pacote = (1,ack,"recebido".encode() )
    pacote_serializado = dumps(pacote)
    client.sendto(pacote_serializado, server_adress)
    return

threading.Thread(target = Send).start()
threading.Thread(target = receive).start()