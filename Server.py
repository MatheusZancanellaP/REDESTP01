import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("Nova conexão adicionada ", clientAddress)

    def run(self):
        print("Conexão de:  ", clientAddress)
        # self.csocket.send(bytes("Olá, aqui é do server ",'utf-8'))
        message = ''
        while True:
            data = self.csocket.recv(2048)
            message = data.decode()
            text = message.split(": ", 1)
            if text[1] == 'quit':
                break
            print("messagem do cliente ", message)
            self.csocket.send(bytes(message, 'UTF-8'))
        print("Cliente ", text[0], " desconectado..")


LOCALHOST = "localhost"
PORT = 4444
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server conectado  ")
print("Esperando requisições")
while True:
    server.listen()
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()