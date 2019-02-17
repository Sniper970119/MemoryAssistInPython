# coding=utf-8
import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
f = client.makefile(mode='r')
while True:
    line = f.readline()
    f.write(line)

