import socket
import threading

# Definindo ip do servidor e porta
host= input('Digite o ip do servidor: ')
port = int(input('Digite a porta do: '))
print('')
print('Informações de conexão:')
print("Porta do servidor: ",port)
print("IP do servidor: ",host)

# Inicializando o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lista dos clientes e os seus nomes de usuario
clients = []
nicknames = []

# Funcao para enviar a mensagem de cada usuário a todos os outros
def broadcast(message):
    for client in clients:
        client.send(message)

# Tratamento de mensagens de clientes
def handle(client):
    while True:
        try:
            # Mensagens em Broadcasting 
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removendo e excluindo os clientes
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('iso8859-1'))
            nicknames.remove(nickname)
            break

# Função de recepção / escuta
def receive():
    while True:
        # Aceitar Conexão
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Solicitar e armazenar o nome de usuário
        client.send('NICK'.encode('iso8859-1'))
        nickname = client.recv(1024).decode('iso8859-1')
        nicknames.append(nickname)
        clients.append(client)

        # Imprimir e transmitir nome de usuário
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('iso8859-1'))
        client.send('Connected to server!'.encode('iso8859-1'))

        # Tratamento de Thread para os clientes
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
