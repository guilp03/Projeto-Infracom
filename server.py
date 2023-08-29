from socket import *
from pickle import *

ACK = 0

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", 4433))
print ("Servidor Pronto")
print("--------------------------------Iniciar Chat----------------------------------------")

