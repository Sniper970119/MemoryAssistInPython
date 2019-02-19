# -*- coding:utf-8 -*-
from src.Update.Conf.config import *


class GetIndexFile():
    """
    从服务器获取更新索引文件
    """
    def __init__(self, s):
        self.s = s

    def getFile(self):
        """
        获取服务器索引文件并保存
        :return:
        """
        fileinfo_size = struct.calcsize('128si2s')
        buf = self.s.recv(fileinfo_size)
        if buf:
            filename, filesize, pw = struct.unpack('128si2s', buf)
            # 删除byte转为str后的\x00  用strip也可以
            newFileName = bytes.decode(filename).rstrip('\x00')
            new_filename = './data/fileIndex.properties'
            recvd_size = 0  # 定义已接收文件的大小
            fp = open(new_filename, 'wb')
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = self.s.recv(1024)
                    recvd_size += len(data)
                else:
                    data = self.s.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            if DEBUG and VERSION_CONTROL_DEBUG:
                print('{SYS}{VERSION_CONTROL_DEBUG}index file has been receive, filesize is ' + str(filesize))


if __name__ == '__main__':
    GetIndexFile().getFile()
