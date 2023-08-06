from socket import *

# Inicializando o socket, passando a versao do protocolo IP (IPv4) e o protocolo de transporte (UDP)
client = socket(AF_INET, SOCK_DGRAM)
# Enviando os dados para o servidor
try:
    # Recebe do usuario o nome do arquivo a ser enviado
    file_name = str(input('Digite o nome do arquivo: '))
    # Envia o nome do arquivo que sera enviado (em bytes) para o servidor, passando a tupla (IP, porta) do socket do servidor
    client.sendto(file_name.encode(), ('127.0.0.1', 7000))
    # Cria uma variavel pra armazenar o caminho onde o arquivo que sera usado para o envio esta, incluindo tambem o nome dele
    path = './arquivos/' + file_name
    # Abre o arquivo com permissao de leitura binaria
    file =  open(path, mode="rb")
    # Envia o arquivo enquanto houver pacotes a serem enviados
    while True:
        # Divide o arquivo em pacotes de no maximo 1024 bytes
        data = file.read(1024)
        # Quando acabarem os pacotes, encerra o while
        if (not data):
            break
        # Envia os pacotes para o servidor, passando os pacotes e a tupla (IP, porta) do socket do servidor
        client.sendto(data, ('127.0.0.1', 7000))
    # Encerra a edicao do arquivo
    file.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
# Recebendo de volta o arquivo do servidor
try:
    with open("./arquivos/new_" + file_name, 'wb') as file:
        while True:
             # Divide o arquivo em pacotes de no maximo 1024 bytes
            data = client.recv(1024)
            # Define o tempo maximo de execucao do socket do cliente, enquanto esta recebendo de volta o arquivo do servidor (2 segundos)
            client.settimeout(2)
            # Quando acabarem os pacotes, encerra o while
            if (not data):
                break
            # Escreve os bytes do arquivo recebido no novo arquivo
            file.write(data)
except Exception as error:
    print("Algo deu Errado")
    print(error)
    # Caso encontre um erro, garante que o socket sera fechado
    client.close()