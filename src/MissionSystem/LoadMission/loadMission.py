# -*- coding:utf-8 -*-
from src.Conf.config import *
from src.MissionSystem.LoadMission.tools import decodeText
from src.MissionSystem.LoadMission.tools import loadMissionFile


class LoadMission():
    """
    读取文件子系统。调用类，任务由被调用者完成。
    """
    def __init__(self, filename='data/mission.dat'):
        self.fileName = filename
        # 初始化解密工具
        self.decodeTools = decodeText.DecodeText()
        # 初始化读取工具
        self.loadTools = loadMissionFile.LoadMissionFile(fileName=filename)

    def loadMission(self):
        """
        读取任务文件,读取失败直接删除该文件
        :return:
        """
        try:
            # 获取加密文件内容
            encodeText = self.loadTools.loadFile()
            # 解密加密内容
            list = self.decodeTools.decodeing(encodeText)
            # 返回列表
            returnList = []
            # 获取当日时间
            today = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d').strftime(
                "%Y-%m-%d")
            # 对当日任务完成情况置为False
            for each in list:
                if each['nextTime'] == today:
                    each['isFinish'] = False
                returnList.append(each)
            return returnList
        except:
            # 处理非异常情况，即第一次打开软件的空数据文件
            if os.path.getsize(self.fileName) == 0:
                return []
            # 反正读取不了  删了吧  -.-
            os.remove(self.fileName)
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{W}{MISSION_DEBUG} can not load mission,file has been delete')
            # 返回None作为调用者知道读取失败的信息
            return None


# 进行读取文件的子系统测试
if __name__ == '__main__':
    l = LoadMission('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    data = l.loadMission()
    print(data)
