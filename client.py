from socket import *
from struct import *
ACK = 0
SEQ = 0
FIN = 0

handshake_packet = Struct('I I')
handshake_unpack = Struct('I I I')
usuario = input("Escolha seu nome de usuario: ")
client = socket(AF_INET, SOCK_DGRAM)
unpack_len = 'I'
#Handshake
while True:
    try:
        pacote = (SEQ, 1)
        pacote_handshake = handshake_packet.pack(*pacote)
        client.sendto(pacote_handshake, ("127.0.0.1", 4433))
        print("Tentando Conexão...")
        client.settimeout(0.009)
        data, sender = client.recvfrom(1024)
        pacote_resposta = handshake_unpack.unpack(data)
        if pacote_resposta[2] == 1 and pacote_resposta[1] == 1:
            SEQ += 1
            print("Conexão Estabelecida")
            break
    except timeout:
            print("timeout ocorreu")
            print("sistema tentará envio mais uma vez")
            print("_______________________________________________")    
            continue
        
while True:
    try:
        msg = input("Mensagem: ") + "\n"
        len_mensagem = len(msg)
        UDP_Packet_Data = Struct(f'I I I {len_mensagem}s')
        mensagem = msg.encode()
        pacote = (SEQ, ACK, FIN, len_mensagem, mensagem)
        pacote_udp = UDP_Packet_Data.pack(*pacote)
        print("Enviando...")
    except Exception as error:
        print("Algo deu Errado")
        print(error)
        client.close()
        break
    while True:
        try:
            client.sendto(pacote_udp, ("127.0.0.1", 4433))
            print("Enviado!")
            client.settimeout(0.009)
            print("Esperando por ACK...")
            data, sender = client.recvfrom(1024)
            unpack_size = unpack_len.unpack(data[2])
            clientUnpacker = Struct(f'I I I {unpack_size}s')
            pacote_resposta = clientUnpacker.unpack(data)
            responseack = pacote_resposta[1]
            if ACK != responseack:
                print(pacote_resposta[0], pacote_resposta[1], pacote_resposta[2], pacote_resposta[3])
                print("ACK incorreto")
                continue
            break
        except timeout:
            print("timeout ocorreu")
            print("sistema tentará envio mais uma vez")
            print("_______________________________________________")    
            continue
        
    if ACK == 0:
        ACK = 1
    elif ACK == 1:
        ACK = 0
    SEQ += len_mensagem