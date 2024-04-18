from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('localhost', 12000))
print("Connected")

raw = client.recv(1024).decode()
print(raw)