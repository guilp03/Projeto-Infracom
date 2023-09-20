from socket import *
from pickle import *
import threading

SEQ = 0
ACK = 1
server_adress = ("127.0.0.1", 4433)

# Funcoes auxiliares

def retransmitir_pacote(seq, msg):
    pacote = (0,seq,msg.encode())
    pacote_serializado = dumps(pacote)
    client.sendto(pacote_serializado, server_adress)

    return

def Send():
    global server_adress
    global SEQ
    global ACK
    global temporizador
    global recebido
    
    while True:
        msg = input("-> ")
        pacote = (0,SEQ, msg.encode())
        pacote_serializado = dumps(pacote)
        client.sendto(pacote_serializado, server_adress)
        semaforo.release()
        temporizador = threading.Timer(5.0, retransmitir_pacote, args= (SEQ, msg))
        temporizador.start()  

def Receive():
    global server_adress
    global SEQ
    global ACK
    global temporizador
    global recebido
    global sent
    
    semaforo.acquire()
    while True:
        mensagem, sender = client.recvfrom(1024)
        data = loads(mensagem)
        if data[0] == 1:
            if data[1] == SEQ:
                temporizador.cancel()
                if data[2].decode() != "ack":
                    print(data[2].decode())
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
    global server_adress
    pacote = (1,ack,"recebido".encode() )
    pacote_serializado = dumps(pacote)
    client.sendto(pacote_serializado, server_adress)
    return

# Definicao do Socket do client
client = socket(AF_INET, SOCK_DGRAM)

# Threads
semaforo = threading.Semaphore(0)
thread1 = threading.Thread(target = Send)
thread1.start()
Receive()