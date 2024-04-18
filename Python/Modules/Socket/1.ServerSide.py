from socket import *
server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen()
print("Listening..")
connection, address = server.accept()
print("Client Connected", connection, address)
connection.send(bytes('Hi This is bk', 'utf-8'))
print('Data sent!')
