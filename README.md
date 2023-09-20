# Projeto de Infraestrutura de Comunicações
Este projeto tem por objetivo implementar um cliente e um servidor de chat de sala única, onde um cliente enviará um pedido de conexão à sala e a partir de aceito, ele passará a receber todas as mensagens dos outros usuários, além de poder também enviar mensagens.

Instruções para executar os arquivos:

1. Abrir ao menos 3 terminais CMD (1 para o server e 2 ou mais para os client's);
2. Ir até a pasta onde os arquivos de código estão localizados, em cada um dos terminais;
3. Executar os arquivos "server.py" e "client.py" com os comandos 'py server.py' e 'py client.py', (sendo o server em um único terminal e um client em cada terminal adicional);
4. No terminal do server, apenas aparecerá uma mensagem informando que o servidor está pronto e que o chat foi iniciado com sucesso;
5. No(s) termina(is)l do(s) client'(s), digite o comando: 'hi, meu nome eh <nome_do_usuario>' para ingressar na sala de chat, imediatamente após isso, será exibida uma mensagem informando que o client ingressou na sala, em todos os client's conectados, incluindo a si mesmo;
6. A partir de então, é possivel que os client's possam trocar mensagens, de modo que, todas as mensagens são vistas por todos os client's conectados na sala de chat única;
7. Sempre que uma mensagem for do tipo: 'list' uma lista de todos os usuários que estão conectados será exibida apenas no chat do client que requisitou;
8. Sempre que uma mensagem for do tipo: 'bye' o client que a digitou será desconectado do chat de sala única, e uma mensagem informando isso, será exibida em todos os outros client's conectados. Caso ele queria retornar ao chat, precisará voltar ao passo 5.
