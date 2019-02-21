# -*- coding:utf-8 -*-


from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead.Tools import readConfigFile
from src.Server.SystemTools.ConfFileRead.Tools import saveConfigFile


class ConfigFileRead():
    def __init__(self, fileName='./conf/server.ini'):
        self.readConfigFileTools = readConfigFile.ReadConfigFile(fileName=fileName)
        self.saveConfigFileTools = saveConfigFile.SaveConfigFile(fileName=fileName)
        pass

    def readFile(self, configMainName, configSubName):
        """
        读取配置文件
        :param configMainName: 配置文件主名称
        :param configSubName: 配置文件副名称
        :return: 配置信息的值
        """
        message = self.readConfigFileTools.readConfigFile(configMainName=configMainName, configSubName=configSubName)
        return message

    def saveFile(self, configMainName, configSubName, value):
        """
        保存到配置文件
        :param configMainName: 配置文件主名称
        :param configSubName: 配置文件副名称
        :param value: 配置文件的值
        :return:
        """
        self.saveConfigFileTools.saveConfigFile(configMainName=configMainName, configSubName=configSubName, value=value)

