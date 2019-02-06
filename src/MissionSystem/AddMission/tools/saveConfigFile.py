# -*- coding:utf-8 -*-


from src.Conf.config import *


class SaveConfigFile():
    def __init__(self, fileName='../conf/mission.ini'):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName

    def saveConfigFile(self, missionId):
        """

        :param missionId: 需要保存的任务id （int 或者 string）
        :return:
        """
        # 防御编程  若messionId不是string，转换则在这转换
        if type(missionId).__name__ != 'string':
            missionId = str(missionId).zfill(6)
        # 写回配置文件
        self.config.read(self.fileName)
        self.config.set("MISSION", "missionId", missionId)
        self.config.write(open(self.fileName, "r+"))
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} config has been save in file successfully')




# 配置文件读取测试
if __name__ == '__main__':
    s = SaveConfigFile(fileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini')
    print(s.saveConfigFile(1))
