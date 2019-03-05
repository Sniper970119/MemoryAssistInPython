# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead


class Code100():
    def __init__(self):
        pass

    def respond(self, connect):
        """
        响应代码100
        :param connect: 与客户端的连接
        :return:
        """
        returnCode = str(configFileRead.ConfigFileRead().readFile('VERSION', 'lastest_version'))
        connect.send(returnCode.encode('utf-8'))
