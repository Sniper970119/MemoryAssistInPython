# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
# from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.MessageTransferSystem.Tools.CodeHandle.Code100 import Code100
from src.Server.MessageTransferSystem.Tools.CodeHandle.Code101 import Code101
from src.Server.MessageTransferSystem.Tools.CodeHandle.Code102 import Code102


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
        address = re.findall('\'(.*?)\'', str(self.address))[0]
        address.replace('\.', '\\.')
        # 100代码为返回最新版本号
        if code == '100' or bytes.decode(code) == '100':
            Code100().respond(self.connect)
        # 101代码为返回用户识别码
        elif code == '101'or bytes.decode(code) == '101':
            Code101().respond(self.connect, address)
        # 102代码为处理已经拥有用户识别码的用户发送的数据
        elif code == '102'or bytes.decode(code) == '102':
            Code102().respond(self.connect, address)
            pass
        else:
            print('unknow code, ', code)
        pass

    def handle(self):
        pass
