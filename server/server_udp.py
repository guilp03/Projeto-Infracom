import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 4433))
print ("Servidor Pronto")
try:
    while True:
        arquivo, endereco_client = serverSocket.recvfrom(1024)
        filename = arquivo.decode()
        print(filename)
        with open(arquivo, 'wb') as file:
            while True:
                data = serverSocket.recv(1024)
                print(data)
                if not data:
                    break
                file.write(data)
        with open(arquivo, 'rb') as file:
            for data in file.readlines():
                serverSocket.sendto(data, endereco_client)
        serverSocket.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close()