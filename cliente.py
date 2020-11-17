import socket
import threading

# Definindo ip do servidor e porta
host= input('Digite o ip do servidor: ')
port = int(input('Digite a porta do: '))
print('')
print('Informações de conexão:')
print("Porta do servidor: ",port)
print("IP do servidor: ",host)
print('')
# Escolhendo um nome de usuário
print(" ")
print("Seja Bem vindo!!!")
print(" ")
nickname = input("Qual seria seu Usuario: ")

# Conectando ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Ouvindo o Servidor e Enviando o Apelido
def receive():
    while True:
        try:
            # Receber mensagem do servidor
            # se recebermos 'NICK' enviamos nosso nome de usuário
            message = client.recv(1024).decode('iso8859-1')
            if message == 'NICK':
                client.send(nickname.encode('iso8859-1'))
            else:
                print(message)
        except:
            # Fechar conexão quando houver erro
            print("An error occured!")
            client.close()
            break

            # Envio de mensagens ao servidor
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('iso8859-1'))
        

# Tratamento de Thread para os clientes
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
