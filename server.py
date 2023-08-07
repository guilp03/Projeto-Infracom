from socket import *

# Inicializando o Socket, passando a versao do protocolo IP (IPv4) e o protocolo de transporte (UDP)
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Define o socket do servidor como tendo o IP do localhost ('') e a porta 7000
serverSocket.bind(('', 7000))
print ("O servidor está pronto")
# Recebendo os dados do cliente
try:
    # Recebe o nome do arquivo que sera recebido do cliente (em bytes) e a tupla (IP, Porta) do socket do cliente (em pacotes de até 1024 bytes)
    arquivo, endereco_client = serverSocket.recvfrom(1024)
    print("O cliente possui socket: ", endereco_client)
    # Resgata a string do nome do arquivo dos bytes recebidos
    filename = arquivo.decode()
    print("O arquivo recebido será: " + filename)
    # Cria uma variavel pra armazenar o caminho onde o arquivo que sera recebido esta, incluindo tambem o nome dele
    path = './' + filename
    # Abre o arquivo com permissao de escrita binaria
    file = open(path, mode="wb")
    # Recebe o arquivo enquanto houver pacotes a serem recebidos
    while True:
        # Recebe o arquivo de fato (em bytes) e a tupla (IP, Porta) do socket do cliente em pacotes de ate 1024 bytes
        data, client_adress  = serverSocket.recvfrom(1024)
        # Define o tempo maximo de execucao do socket do servidor, enquanto esta recebendo o arquivo do cliente (2 segundos)
        serverSocket.settimeout(2)
        # Quando acabarem os pacotes, encerra o while
        if (not data):
            break
        # Escreve os bytes do arquivo recebido no arquivo que teve seu conteudo apagado
        file.write(data)
    # Encerra a edicao do arquivo
    file.close()
except Exception as error:
    print("Algo deu Errado")
    print(error)
# Enviando de volta o arquivo para o cliente 
try:
    with open(arquivo, 'rb') as file:
        # Envia de volta para o cliente o arquivo antes recebido, enquanto houver pacotes a serem enviados
        while True:
            # Divide o arquivo em pacotes de no maximo 1024 bytes
            data = file.read(1024)
            # Define o tempo maximo de execucao do socket do servidor, enquanto esta enviando de volta o arquivo para o cliente (2 segundos)
            serverSocket.settimeout(2)
            # Quando acabarem os pacotes, encerra o while
            if (not data):
                break
            # Envia para o cliente, passando os pacotes e a tupla (IP, porta) do seu socket, resgatado quando recebeu o nome do arquivo
            serverSocket.sendto(data, endereco_client)
except Exception as error:
    print("Algo deu Errado")
    print(error)
    # Caso encontre um erro, garante que o socket sera fechado
    serverSocket.close()