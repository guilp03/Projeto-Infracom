from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 4433))
print ("Servidor Pronto")

try:
    while True:
        message, endereco_client = serverSocket.recvfrom(1024)
        msg = message.decode()
        serverSocket.sendto(msg.encode(),endereco_client)
        if msg == "sair\n":
            break
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close() 