from socket import *

client = socket(AF_INET, SOCK_DGRAM)
try:
    file_name = str(input('digite o nome do arquivo: '))
    client.sendto(file_name.encode(), ('127.0.0.1', 7000))
    path = './' + file_name
    file =  open(path, mode="rb")
    while True:
        data = file.read(1024)
        if (not data):
            break
        client.sendto(data, ('127.0.0.1', 7000))
    file.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)  
try:
    with open("new_" + file_name, 'wb') as file:
        while True:
            data = client.recv(1024)
            print(data)
            client.settimeout(2)
            if (not data):
                break
            file.write(data)
            
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()