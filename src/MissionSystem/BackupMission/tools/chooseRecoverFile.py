# -*- coding:utf-8 -*-

from src.Conf.config import *


class ChooseRecoverFile():
    def __init__(self, filePath='../data/bkup/mbk/'):
        self.filePath = filePath
        pass

    def choose(self):
        """
        选择最新的备份作为备份文件
        :return:
        """
        try:
            # 获取备份文件列表
            files = os.listdir(self.filePath)
            maxFileName = None
            maxFileTime = 0
            # 寻找最新的备份文件
            for file in files:
                # 初始化为第一个文件最后修改时间的时间戳
                if maxFileTime == 0:
                    maxFileTime = os.path.getctime(self.filePath + '/' + file)
                    maxFileName = file
                # 寻找最小时间戳
                else:
                    if maxFileTime < os.path.getctime(self.filePath + '/' + file):
                        maxFileTime = os.path.getctime(self.filePath + '/' + file)
                        maxFileName = file
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{MISSION_DEBUG} latest backup file has been chosen' + maxFileName)
            # 返回最小时间戳的文件名
            return maxFileName
        except Exception, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'MissionSystem-BackupMission-chooseRecoverFile',
                '|wrongMessage': str(e)
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
            return None
