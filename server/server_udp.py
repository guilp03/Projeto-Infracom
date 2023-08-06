from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 7000))
print ("Servidor Pronto")
try:
    arquivo, endereco_client = serverSocket.recvfrom(1024)
    filename = arquivo.decode()
    path = './' + filename

    print(filename)
    file = open(path, mode="wb")
    while True:
        data, client_adress  = serverSocket.recvfrom(1024)
        serverSocket.settimeout(2)
        if (not data):
            break
        file.write(data)
    file.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    
try:
    with open(arquivo, 'rb') as file:
        while True:
            data = file.read(1024)
            serverSocket.settimeout(2)
            if (not data):
                break
            serverSocket.sendto(data, endereco_client)
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close()