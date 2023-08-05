from socket import *

client = socket(AF_INET, SOCK_DGRAM)
try:
    file_name = str(input('digite o nome do arquivo: '))
    client.sendto(file_name.encode(), ('127.0.0.1', 7000))
    path = './' + file_name
    testfile =  open(path, mode="rb")
    while True:
        data = testfile.read(1024)
        if (not data):
            break
        client.sendto(data, ('127.0.0.1', 7000))
    testfile.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()
    
try:
    with open("new_" + file_name, 'wb') as testfile:
        while True:
            data = client.recv(1024)
            if not data:
                break
            testfile.write(data)
            
except Exception as error:
    print("Algo deu Errado")
    print(error)
    client.close()