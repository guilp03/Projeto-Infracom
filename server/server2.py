import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 4433))
print ("Servidor Pronto")
try:
    while True:
        arquivo, endereco_client = serverSocket.recvfrom(1024)
        print("1")
        filename = arquivo.decode()
        print("1")
        size = int(serverSocket.recv(1024).decode())
        print("1")
        print(f"Receiving {filename}, size: {size}")
        print("1")
        with open(arquivo, 'wb') as file:
            for i in range(size):
                data = serverSocket.recv(1024)
                print(data)
                file.write(data)
        with open(arquivo, 'rb') as file:
            for data in file.readlines():
                serverSocket.sendto(data, endereco_client)
        break
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close()