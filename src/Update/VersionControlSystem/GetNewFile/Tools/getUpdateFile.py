# -*- coding:utf-8 -*-
from src.Update.Conf.config import *


class GetUpdateFile():
    """
    获取服务器发送过来的更新文件
    """
    def __init__(self, s):
        self.s = s
        pass

    def get(self):
        """
        获取服务器发送到客户端的更新文件，并按照更新索引文件的地址保存
        :return:
        """
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
    """
    解析索引文件
    """
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

    def get(self, key, default_value='./'):
        """
        获取应该存放的路径
        :param key: 文件名
        :param default_value: 默认返回值（如果没做规定则默认放到根目录）
        :return:
        """
        if key in self.properties:
            return self.properties[key]
        return default_value

    def getLength(self):
        """
        回去索引列表中更新文件长度
        :return:
        """
        return len(self.properties)
