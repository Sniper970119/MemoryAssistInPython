# coding=utf-8
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen(10)
sock, addr = server.accept()
while True:
    data = sock.recv(1024)
    data = str(addr) + ':' + str(data)
    print(data.decode('utf-8'))
    returnData = raw_input()
    sock.send(returnData.encode('utf-8'))

