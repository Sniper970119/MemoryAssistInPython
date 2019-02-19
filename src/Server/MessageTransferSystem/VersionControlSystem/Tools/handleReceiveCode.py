# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class HandleReceiveCode():
    """
    处理接受的请求代码
    """
    def __init__(self, connect, address):
        self.connect = connect
        self.address = address
        pass

    def getNumber(self):
        """
        获取客户端发送代码，进行返回
        :return:
        """
        code = self.connect.recv(1024)
        if DEBUG and VERSION_CONTROL_DEBUG:
            print('Accept new connection(mes) from {0},code is {1}'.format(self.address, code))
        # 100代码为返回最新版本号
        if code == '100':
            # 这里应该是读服务器端的配置文件读取最新版本号
            returnCode = 'v1.0'.encode('utf-8')
            self.connect.send(returnCode)
            pass
        pass

    def handle(self):
        pass
