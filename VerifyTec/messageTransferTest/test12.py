# coding=utf-8
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    message = raw_input()
    client.send(message.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

