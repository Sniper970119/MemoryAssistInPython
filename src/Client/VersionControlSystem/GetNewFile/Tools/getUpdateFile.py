# -*- coding:utf-8 -*-
from src.Client.Conf.config import *


class GetUpdateFile():
    def __init__(self, s):
        self.s = s
        pass

    def get(self):
        file_path = './data/fileIndex.properties'
        property = Properties(file_path)  # 读取文件
        loopTime = property.getLength()
        while loopTime != 0:
            loopTime = loopTime - 1
            fileinfo_size = struct.calcsize('128si2s')
            buf = self.s.recv(fileinfo_size)
            if buf:
                filename, filesize, pwd = struct.unpack('128si2s', buf)


                # 删除byte转为str后的\x00  用strip也可以
                newFileName = bytes.decode(filename).rstrip('\x00')
                # 得到文件路径前缀
                dirPrefix = property.get(newFileName)
                new_filename = os.path.join(dirPrefix, '' + newFileName)
                print('file new name is {0}, filesize if {1}'.format(new_filename, filesize))

                recvd_size = 0  # 定义已接收文件的大小
                fp = open(new_filename, 'wb')
                print('start receiving...')
                while not recvd_size == filesize:
                    if filesize - recvd_size > 1024:
                        data = self.s.recv(1024)
                        recvd_size += len(data)
                    else:
                        data = self.s.recv(filesize - recvd_size)
                        recvd_size = filesize
                    fp.write(data)
                fp.close()
                print('end receive...')
        print('finish file receive')


class Properties:
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception:
            # raise Exception
            print("read file exception ...")
        else:
            fopen.close()

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def getLength(self):
        return len(self.properties)
