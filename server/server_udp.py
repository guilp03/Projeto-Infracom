import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 4433))
print ("Servidor Pronto")
try:
    while True:
        message, endereco_client = serverSocket.recvfrom(1024)
        filename = message.decode('latin-1')
        with open(filename, 'wb') as file:
            while True:
                data, _ = serverSocket.recv(1024)
                if not data:
                    break
                file.write(data)
        with open(filename, 'rb') as file:
            for data in file:
                serverSocket.sendto(data, endereco_client)
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close()