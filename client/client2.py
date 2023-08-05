import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    file_name = str(input('digite o nome do arquivo: '))
    client.sendto(file_name.encode(), ('127.0.0.1', 4433))
    while True:
        with open(file_name, 'rb') as arq:
            for dados_arquivo in arq.read(1024):
                print(dados_arquivo)
                serializar = struct.Struct("{}s {}s".format(len(file_name), len(dados_arquivo)))
                dados_upload = serializar.pack(*[file_name.encode(), dados_arquivo])

                serializar = struct.Struct("{}s {}s".format(len(file_name), len(dados_arquivo)))
                client.sendto(dados_upload,('127.0.0.1', 4433))

        with open(file_name + "_new", 'wb') as file:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                file.write(data)
        client.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()