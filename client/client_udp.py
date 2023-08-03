import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        file_name = str(input('digite o nome do arquivo: '))
        with open(file_name, 'rb') as file:
            for data in file.readlines():
                client.sendto(data, ('127.0.0.1', 4433))
        new_file, _ = client.recvfrom(1024)
        with open(new_file, 'wb') as file:
            while True:
                data = client.recvfrom(1024)
                if not data:
                    break
                file.write(data)
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()