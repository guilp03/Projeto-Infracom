import socket
import os

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', 4433))
print ("Servidor Pronto")
try:
    while True:
        message, endereco_client = serverSocket.recvfrom(1024)
        nome_arquivo, conteudo = message.split(b'|', 1)
        with open(nome_arquivo, 'wb') as file:
            file.write(conteudo)
        os.rename(nome_arquivo, "renomeado.txt")
        with open(file, "rb") as file:
            while True:
                dados = file.read(1024)
                if not dados:
                    break
        serverSocket.sendto(dados,endereco_client)
        serverSocket.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    serverSocket.close()