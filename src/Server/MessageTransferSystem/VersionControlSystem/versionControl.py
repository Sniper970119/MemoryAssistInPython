# -*- coding:utf-8 -*-
from src.Server.Conf.config import *

from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendInexFile
from src.Server.MessageTransferSystem.VersionControlSystem.Tools import sendUpdateFile


class VersionControl():
    def __init__(self, filePath='./updateFile/'):
        self.filePath = filePath
        self.listen()

    def listen(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.bind(('127.0.0.1', 9000))
            self.s.listen(10)
        except socket.error as msg:
            print(msg)
        print('file waiting for connection...')
        while 1:
            conn, addr = self.s.accept()
            t = threading.Thread(target=self.sendIndexFile, args=(conn, addr))
            # t = threading.Thread(target=self.sendUpdateFile, args=(conn, addr))
            t.start()
        pass

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
    VersionControl(filePath='F:\python17\pythonPro\MemortAssit\updateFile/').listen()
