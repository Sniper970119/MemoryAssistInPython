# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class SendUpdateFile():
    """
    发送更新文件
    """
    def __init__(self, connect, address, filePath='./updateFile/'):
        self.properties = {}
        self.connect = connect
        self.address = address
        self.filePath = filePath
        self.fileSize = 0
        pass

    def findFile(self):
        """
        发送更新文件
        :return:
        """
        files = os.listdir(self.filePath)
        for each in files:
            fileAbsPath = self.filePath+each
            self.send(fileAbsPath)
        self.connect.close()
        if DEBUG and VERSION_CONTROL_DEBUG:
            print('{SYS}{VERSION_CONTROL_DEBUG}update file has been send, filesize is ' + str(self.fileSize))

    def send(self, fileName):
        if os.path.isfile(fileName):
            fhead = struct.pack('128si2s', bytes(os.path.basename(fileName).encode('utf-8')), os.stat(fileName).st_size,
                                b'pw')
            self.connect.send(fhead)
            self.fileSize += os.stat(fileName).st_size
            fp = open(fileName, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print('{0} file send over...'.format(fileName))
                    break
                self.connect.send(data)
            fp.close()

        pass



