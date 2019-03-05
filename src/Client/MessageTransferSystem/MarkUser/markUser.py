# -*- coding:utf-8 -*-
from src.Client.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead


class MarkUser():
    def __init__(self):
        try:
            self.configFileReadTools = configFileRead.ConfigFileRead()
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((SERVER_IP, SERVER_MES_PORT))


        except socket.error as msg:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MessageTransferSystem-VersionControl-versionControl',
                '|wrongMessage': msg
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

    def judge(self):
        """
        读取用户识别码，如果没有识别码向服务器发送请求，如果有识别码，向服务器发送识别码和访问次数。
        :return:
        """
        userCode = self.configFileReadTools.readFile('USER_CODE', 'user_code')
        if userCode != '':
            # 如果当前没有用户识别码，向服务器请求识别码，并写回配置文件
            # 发送代码101 作为向服务器请求新的用户识别码
            self.s.send('101')
            returnData = self.s.recv(1024)
            # 写回配置文件
            self.configFileReadTools.saveFile('USER_CODE', 'user_code', returnData)
