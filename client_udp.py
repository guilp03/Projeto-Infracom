import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        file_name = input("file path: ")
        with open(file_name, "rb") as file:
            while True:
                dados = file.read(1024)
                if not dados:
                    break
        data = file_name.encode() + b'|' + dados
        client.sendto(data, ("127.0.0.1", 4433))
        client.sendto(b"", ("127.0.0.1", 4433))
        data, sender = client.recvfrom(1024)
        nome_arquivo, conteudo = data.split(b'|', 1)
        print(sender[0] + ": " + nome_arquivo)
        client.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()