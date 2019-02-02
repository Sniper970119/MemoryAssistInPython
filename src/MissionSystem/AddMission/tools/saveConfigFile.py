# -*- coding:utf-8 -*-


from src.Conf.config import *


class SaveConfigFile():
    def __init__(self, fileName='../conf/mission.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def saveConfigFile(self, messionId):
        """

        :param messionId: 需要保存的任务id （int 或者 string）
        :return:
        """
        # 防御编程  若messionId为转换则在这转换
        if type(messionId).__name__ != 'string':
            messionId = str(messionId).zfill(4)
        # 写回配置文件
        self.config.read(self.fileName)
        self.config.set("MISSION", "missionId", messionId)
        self.config.write(open(self.fileName, "r+"))
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} config has been save in file successfully')




# 配置文件读取测试
if __name__ == '__main__':
    s = SaveConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini')
    print(s.saveConfigFile(1))
