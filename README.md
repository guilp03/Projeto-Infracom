# Projeto de Infraestrutura de Comunicações
Este projeto tem por objetivo implementar um cliente e um servidor de chat de sala única, onde um cliente enviará um pedido de conexão à sala e a partir de aceito, ele passará a receber todas as mensagens dos outros usuários, além de poder também enviar mensagens.

Será utilizada a biblioteca socket da linguagem Python para implementar uma conexão UDP para transferencia de arquivos com envio e devolução, de modo que, um cliente envia para um servidor e depois recebe o mesmo arquivo de volta. Os arquivos devem ser enviados em pacotes de até 1024 bytes.

Instruções para executar os arquivos:

1. Abrir dois terminais CMD;
2. Ir até a pasta onde os arquivos de código estão localizados, em cada um dos terminais;
3. Executar os arquivos server.py e client.py com os comandos 'py server.py' e 'py client.py', um em cada terminal;
4. No terminal do cliente, quando solicitado, digite o nome do arquivo que quer enviar;
5. O envio do arquivo será realizado primeiramente do cliente para o servidor e posteriormente do servidor para o cliente.