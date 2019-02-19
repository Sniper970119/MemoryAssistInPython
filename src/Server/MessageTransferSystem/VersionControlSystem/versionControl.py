# -*- coding:utf-8 -*-
from src.Server.Conf.config import *

from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendInexFile
from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendUpdateFile
from src.Server.MessageTransferSystem.VersionControlSystem.Tools import handleReceiveCode


class VersionControl():
    def __init__(self, filePath='./updateFile/'):
        self.filePath = filePath
        threading.Thread(target=self.listenFile).start()
        threading.Thread(target=self.listenMessage).start()


    def listenMessage(self):
        try:
            self.messageSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.messageSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.messageSocket.bind(('127.0.0.1', 9001))
            self.messageSocket.listen(10)
        except socket.error as msg:
            print(msg)
        print('message waiting for connection, ')
        while 1:
            conn, addr = self.messageSocket.accept()
            t = threading.Thread(target=self.handlerReceiveCode, args=(conn, addr))
            t.start()
        pass

    def listenFile(self):
        try:
            self.fileSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.fileSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.fileSocket.bind(('127.0.0.1', 9000))
            self.fileSocket.listen(10)
        except socket.error as msg:
            print(msg)
        print('file waiting for connection...')
        while 1:
            conn, addr = self.fileSocket.accept()
            t = threading.Thread(target=self.sendIndexFile, args=(conn, addr))
            # t = threading.Thread(target=self.sendUpdateFile, args=(conn, addr))
            t.start()
        pass

    def handlerReceiveCode(self, connect, address):
        self.handleReceiveCodeTools = handleReceiveCode.HandleReceiveCode(connect,address)
        self.handleReceiveCodeTools.getNumber()


    def sendIndexFile(self, connect, address):
        self.sendIndexFileTools = sendInexFile.SendIndexFile(connect, address)
        self.sendIndexFileTools.sendFile()
        self.sendUpdateFileTools = sendUpdateFile.SendUpdateFile(connect, address, filePath=self.filePath)
        self.sendUpdateFileTools.findFile()

    def sendUpdateFile(self, connect, address):
        self.sendUpdateFileTools = sendUpdateFile.SendUpdateFile(connect, address, filePath=self.filePath)
        self.sendUpdateFileTools.findFile()


if __name__ == '__main__':
    # VersionControl().listen()
    VersionControl(filePath='F:\python17\pythonPro\MemortAssit\updateFile/').listenFile()
