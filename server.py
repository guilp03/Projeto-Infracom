from socket import *
from struct import *

ACK = 0
SEQ = 0

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 4433))
print ("Servidor Pronto")
handshake_pack = ('I I I')
unpack_len = 'I'

while True:
    data, sender = serverSocket.recvfrom(1024)

    if unpack_len.unpack(data[0]) == 0 and unpack_len.unpack(data[1]) == 1:
        #iniciar o handshake
        pacote = (SEQ, 1, ACK)
        handshake_packet = handshake_pack.pack(*pacote)
        while True:
            serverSocket.sendto(handshake_packet, sender)
            print("Pedido de Conexão recebido!")
            print("Confirmando...")
            serverSocket.settimeout(0.009)
            data, sender = serverSocket.recvfrom(1024)

