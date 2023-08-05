import struct

arquivo = "imagem.jpg"

with open(arquivo, 'rb') as arq:
    dados_arquivo = arq.read()
    serializar = struct.Struct("{}s {}s".format(len(arquivo), len(dados_arquivo)))
    dados_upload = serializar.pack(*[arquivo.encode(), dados_arquivo])

    serializar = struct.Struct("{}s {}s".format(len(arquivo), len(dados_arquivo)))
    
    print(type(dados_upload))