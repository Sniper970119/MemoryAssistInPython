# -*- coding:utf-8 -*-
from src.Client.recitationSystem.addRecitation.tools import loadConfigFile, saveConfigFile, addRecitationToList
from src.Client.SystemTools.SaveFiles import saveFiles


class AddRecitation():
    """
    该类负责增加任务相关事宜，属于调用类，调用各种方法完成目的。
    """

    def __init__(self, confFileName='../conf/recitation.ini', dataFileName='../data/recitation.dat'):
        # 初始化工具
        self.loadConfigTools = loadConfigFile.LoadConfigFile(fileName=confFileName)
        self.addMissionTools = addRecitationToList.AddRecitationToList()
        self.saveConfigTools = saveConfigFile.SaveConfigFile(fileName=confFileName)
        self.saveMissionTools = saveFiles.SaveFiles(filename=dataFileName)
        pass

    def addRecitation(self, list, recitationId, question, answer, weight):
        """

        :param list:  目标list
        :param recitationId: 任务id（string
        :param question: 问题
        :param answer: 答案
        :param weight: 权重
        :return: 添加后的list
        """
        if recitationId is None:
            # 读取配置文件并自增+1
            nextRecitationId = self.loadConfigTools.loadConfigFile()
            nextRecitationId = nextRecitationId + 1
            # 写回到配置文件
            self.saveConfigTools.saveConfigFile(nextRecitationId)
            recitationId = nextRecitationId
        # 添加到列表并获取到返回列表
        list = self.addMissionTools.addRecitation(list=list, recitationId=recitationId, question=question,
                                                  answer=answer, weight=weight)
        # 保存到文件
        self.saveMissionTools.saveFiles(list)
        return list


# 对添加任务子系统的测试
if __name__ == '__main__':
    pass
    # a = AddMission()
    # l = loadMission.LoadFiles("F:\python17\pythonPro\MemortAssit\data\mission.dat")
    # list = l.loadMission()
    #
    # a = AddMission(confFileName='F:\python17\pythonPro\MemortAssit\conf\mission.ini',
    #                dataFileName='F:\python17\pythonPro\MemortAssit\data\mission.dat')
    # a.addMission(list=list, bookName='testBook', missionRange='testMission')
