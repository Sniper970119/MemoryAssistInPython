# -*- coding:utf-8 -*-


from src.Conf.config import *


class LoadConfigFile():
    def __init__(self, fileName='../conf/mission.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def loadConfigFile(self):
        """
        读取配置文件
        :return:下个id（int）
        """
        # 读取配置文件
        self.config.readfp(open(self.fileName))
        missionId = self.config.get('MISSION', 'missionId')
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} config has been load from file successfully')
        return int(missionId)



# 配置文件读取测试
if __name__ == '__main__':
    l = LoadConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini')
    print(l.loadConfigFile())
