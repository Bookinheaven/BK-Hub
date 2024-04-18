from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 12000))
while True:
    data = client.recv(1024)
    print(f"Server: {data.decode()}")
    text = input("Type: ")
    if text == 'exit':
        client.close()
        quit()
    else:
        client.send(bytes(text, 'utf-8'))
