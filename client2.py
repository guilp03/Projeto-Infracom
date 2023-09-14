from socket import *
from pickle import *

SEQ = 0

server_adress = ("127.0.0.1", 4433)
client = socket(AF_INET, SOCK_DGRAM)
#Handshake
while True:
    msg = input("Digite Sua Mensagem: ")
    pacote = (SEQ, msg.encode())
    pacote_serializado = dumps(pacote)
    while True:
        try:
            client.sendto(pacote_serializado,server_adress)
            client.settimeout(1)
            mensagem, sender = client.recvfrom(1024)
            data = loads(mensagem)
            if msg == "list":
                if data[0] == SEQ:
                    print(data[1])
                    if SEQ == 0:
                        SEQ = 1
                    else:
                        SEQ = 0
                break
            else:   
                if data[0] == SEQ:
                    print(data[1].decode())
                    if SEQ == 0:
                        SEQ = 1
                    else:
                        SEQ = 0
                break
        except timeout:
            print("Times Estourou! Reenviando...")
            continue