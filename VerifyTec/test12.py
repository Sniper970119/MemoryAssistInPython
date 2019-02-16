# coding=utf-8
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
while True:
    returnData = raw_input("input:")
    client.send(returnData.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode('utf-8'))

