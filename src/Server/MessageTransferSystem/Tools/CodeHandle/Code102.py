# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead


class Code102():
    def __init__(self):
        pass

    def respond(self, connect):
        """
        响应代码102
        :param connect: 与客户端的连接
        :return:
        """
        # 向客户端发送连接标记
        connect.send('user_code'.encode('utf-8'))
        userCode = connect.recv(1024)
        connect.send('time'.encode('utf-8'))
        time = connect.recv(1024)
        # 将数据更新到数据中
        # -------------------------------------------------------------------------
