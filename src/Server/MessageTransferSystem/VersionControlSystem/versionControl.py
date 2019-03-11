# -*- coding:utf-8 -*-
from src.Server.Conf.config import *

from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendInexFile
from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendUpdateFile
from src.Server.MessageTransferSystem.Tools import handleReceiveCode


class VersionControl():
    """
    进行版本控制，调用来
    """
    def __init__(self, filePath='./updateFile/'):
        self.filePath = filePath
        threading.Thread(target=self.listenFile).start()
        threading.Thread(target=self.listenMessage).start()


    def listenMessage(self):
        """
        监听消息端口，根据客户端发送的消息代码做出响应
        :return:
        """
        try:
            self.messageSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.messageSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            host = socket.gethostname()
            # print(host)
            if DEBUG:
                host = '127.0.0.1'
            self.messageSocket.bind((host, 9001))
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
        """
        监听文件端口，向客户端发送更新文件
        :return:
        """
        try:
            self.fileSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.fileSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            host = socket.gethostname()
            if DEBUG:
                host = '127.0.0.1'
            self.fileSocket.bind((host, 9000))
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
        """
        处理响应代码
        :param connect: socket连接
        :param address: socket地址
        :return:
        """
        self.handleReceiveCodeTools = handleReceiveCode.HandleReceiveCode(connect, address)
        self.handleReceiveCodeTools.getNumber()


    def sendIndexFile(self, connect, address):
        """
        处理发送索引文件
        :param connect: socket连接
        :param address: socket地址
        :return:
        """
        self.sendIndexFileTools = sendInexFile.SendIndexFile(connect, address)
        self.sendIndexFileTools.sendFile()
        self.sendUpdateFileTools = sendUpdateFile.SendUpdateFile(connect, address, filePath=self.filePath)
        self.sendUpdateFileTools.findFile()

    def sendUpdateFile(self, connect, address):
        """
        处理发送更新文件
        :param connect: socket连接
        :param address: socket地址
        :return:
        """
        self.sendUpdateFileTools = sendUpdateFile.SendUpdateFile(connect, address, filePath=self.filePath)
        self.sendUpdateFileTools.findFile()


if __name__ == '__main__':
    # VersionControl().listen()
    VersionControl(filePath='F:\python17\pythonPro\MemortAssit\updateFile/').listenFile()
