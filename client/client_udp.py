import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        file_name = str(input('digite o nome do arquivo: '))
        client.sendto(file_name.encode(), ('127.0.0.1', 4433))
        with open(file_name, 'rb') as file:
            for data in file.readlines():
                client.sendto(data, ('127.0.0.1', 4433))
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