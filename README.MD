#Trabalho Redes
 O trabalho foi realizado em 2 arquivos, nos quais observa-se que no servidor.py são dados os comandos para realizar a criação da conexão em si. Dessa maneira, nota-se que o servidor fica em modo listening e cria uma nova thread, que permanece com o estado de ativa até que o cliente se desconecte com a mensagem quit. Entretanto, caso a mensagem seja diferente, o servidor irá pegar a mensagem que recebeu e  a devolve para o cliente, sendo assim um servidor de echo. 
 Trabalho foi desenvolvido no PyCharm/VSC usando a linguagem python 3, para a execução é necessário alguma IDE que entenda python, pois os arquivos são .py 
 Para a execução dos arquivos basta abrir primeiro o servidor.py pelo prompt, digitando seu caminho, uma vez na pasta basta digitar python3 server.py, se for no visualCode, é só executar o arquivo, ou o comando python3 server.py no prompt do VSC.
 Mais detalhes e explicação dos blocos de código funcionais estão comentados no próprio código. 
 Com o servidor conectado, deve-se realizar a abrertura de outro prompt e ir na pasta onde está o client.py, uma vez na pasta, o cliente se conecta com o seguinte comando, que possui 4 argumentos, a linguagem python3, a pasta client.py, o nome do cliente, que pode ser qualquer um, e o servidor, que foi chamado de localhost, com isso o cliente se conectará ao servidor. Ex: "python3 client.py matheus localhost".Isso pode se repetir quantas vezes quiser, basta só abrir outro prompt e mudar o nome do client, para terminar a conexão basta digitar "quit" no terminal do cliente e depois matar o prompt.