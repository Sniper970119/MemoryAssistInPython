# -*- coding:utf-8 -*-
from src.Update.Conf.config import *
from src.Update.VersionControlSystem.GetNewFile import doUpdate
from src.Update.VersionControlSystem.JudgeNeedUpdate import judgeNeedUpdate
from src.Update.SystemTools.ConfFileRead import configFileRead


class VersionControl():
    def __init__(self):
        self.judgeNeedUpdateTools = judgeNeedUpdate.JudgeNeedUpdate()

    def handle(self):
        """
        版本控制一级系统
        :return:
        """
        try:
            needUpdate, version = self.judgeNeedUpdateTools.judge()
            version = bytes.decode(version)
            print(version)
            if needUpdate:
                if messagebox.askokcancel(title='是否更新', message='检测到有新版本，是否更新,更新完成后自动运行'):
                    doUpdate.GetNewFile()
                    configFileRead.ConfigFileRead().saveFile('VERSION', 'version', version)
        except socket.error as msg:
            print('no network')
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'VersionControlSystem-versionControl',
                '|wrongMessage': msg,
                '|没有互联网连接|': '没有互联网连接',
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()

        finally:
            os.system('start run.exe')
