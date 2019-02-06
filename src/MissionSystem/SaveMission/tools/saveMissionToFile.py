# -*- coding:utf-8 -*-
from src.Conf.config import *


class SaveMissionToFile():
    def __init__(self, fileName='../data/mission.dat'):
        self.fileName = fileName

    def saveToFile(self, data):
        """
        保存加密数据到文件
        :param data: 加密数据
        :return:
        """
        # 保存到文件
        self.missionFile = open(self.fileName, 'wb')
        self.missionFile.write(data)
        # 关闭文件流
        self.missionFile.close()
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} file has been write in file successfully')
        pass


if __name__ == '__main__':
    f = open('../../../../data/mission.dat', 'wb')
    print(f.read())
