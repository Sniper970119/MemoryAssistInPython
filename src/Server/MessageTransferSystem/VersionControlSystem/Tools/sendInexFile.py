# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class SendIndexFile():
    """
    发送更新索引文件
    """
    def __init__(self, connect, address):
        if DEBUG and VERSION_CONTROL_DEBUG:
            print('Accept new connection from {0}'.format(address))
        self.connect = connect
        self.address = address

    def sendFile(self):
        """
        发送更新索引文件
        :return:
        """
        filepath = "./data/fileIndex.properties"
        if os.path.isfile(filepath):
            fhead = struct.pack('128si2s', bytes(os.path.basename(filepath).encode('utf-8')), os.stat(filepath).st_size,
                                b'pw')
            self.connect.send(fhead)
            fp = open(filepath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print('{0} file send over...'.format(filepath))
                    break
                self.connect.send(data)
        if DEBUG and VERSION_CONTROL_DEBUG:
            print('{SYS}{VERSION_CONTROL_DEBUG}index file has been send, filesize is '+str(os.stat(filepath).st_size))
        pass
