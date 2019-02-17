# -*- coding:utf-8 -*-
from src.Update.Conf.config import *
from src.Client.SystemTools.ConfFileRead import configFileRead


class JudgeNeedUpdate():
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
                '|file': 'VersionControlSystem-GetNewFile-doUpdate',
                '|wrongMessage': msg
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

    def judge(self):
        vision = self.configFileReadTools.readFile('VERSION', 'version')
        # 请求码为100时 返回最新版本号
        self.s.send('100')
        returnData = self.s.recv(1024)
        if vision == returnData:
            return True
        else:
            return False
        pass
