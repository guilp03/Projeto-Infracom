from socket import *
from struct import *
ack = 0
seq = 0
    
usuario = input("Escolha seu nome de usuario: ")
client = socket(AF_INET, SOCK_DGRAM)
unpack_len = 'I'
while True:
    try:
        msg = input("Mensagem: ") + "\n"
        len_mensagem = len(msg)
        UDP_Packet_Data = Struct(f'I I I {len_mensagem}s')
        mensagem = msg.encode()
        pacote = (ack, seq, len_mensagem, mensagem)
        pacote_udp = UDP_Packet_Data.pack(*pacote)
        client.sendto(pacote_udp, ("127.0.0.1", 4433))
        print("Enviando...")
    except Exception as error:
        print("Algo deu Errado")
        print(error)
        client.close()
        break
    while True:
        try:
            client.sendto(pacote_udp, ("127.0.0.1", 4433))
            ack_momento = ack
            print("Enviado!")
            client.settimeout(0.009)
            print("Esperando por ACK...")
            data, sender = client.recvfrom(1024)
            unpack_size = unpack(data[2])
            clientUnpacker = Struct(f'I I I {unpack_size}s')
            pacote_resposta = clientUnpacker(data)
            responseack = pacote_resposta[0]
            #comparar o ack
            #arrumar o timeout
            if not data:
                while not data:
                    client.sendto(msg.encode(), ("127.0.0.1", 4433))
                    #timeout
                    data, sender = client.recvfrom(1024)            

                
                
        except Exception as error:
            print("Algo deu Errado")
            print(error)
            client.close()
            break        