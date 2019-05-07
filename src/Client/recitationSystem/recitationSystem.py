# -*- coding:utf-8 -*-
from src.Client.Conf.config import *

from src.Client.SystemTools.LoadFiles import loadFiles
from src.Client.SystemTools.SaveFiles import saveFiles
from src.Client.recitationSystem.addRecitation import addRecitation
from src.Client.recitationSystem.editRecitation import editRecitation


class RecitationSystem():
    """
    背诵系统，一级子系统。对外提供任务系统的各个功能。
    """

    def __init__(self, confFileName='conf/recitation.ini', dataFileName='data/recitation.dat'):
        # 初始化工具
        self.loadRecitationTools = loadFiles.LoadFiles(filename=dataFileName)
        self.addRecitationTools = addRecitation.AddRecitation(confFileName=confFileName, dataFileName=dataFileName)
        self.editRecitationTools = editRecitation.EditRecitation(filename=dataFileName)
        self.saveRecitationTools = saveFiles.SaveFiles(filename=dataFileName)
        self.list = self.loadRecitation()

    def loadRecitation(self):
        """
        一级子系统的读取任务文件
        :return:
        """
        # 读取任务文件
        list = self.loadRecitationTools.loadFiles(missionType='recitation')
        return list

    def addRecitation(self, question, answer, recitationId=None, weight=10):
        """
        一级子系统的添加任务操作
        :param recitationId: 任务id（string
        :param question: 书名
        :param answer: 任务范围
        :param weight: 权重
        :return: 添加后的list
        """
        # 转换任务id
        if recitationId is not None:
            recitationId = str(recitationId).zfill(6)
        # 调用增加任务工具
        self.addRecitationTools.addRecitation(list=self.list, question=question, answer=answer,
                                              recitationId=recitationId,
                                              weight=weight)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{RECITATION_DEBUG} recitation has been added successful')

    def editRecitation(self, recitationId, question=None, answer=None, weight=10, isEdit=False, isDelete=False):
        """
        一级子系统的编辑任务操作
        :param recitationId: 任务id
        :param question: 问题
        :param answer: 答案
        :param weight: 权重
        :param isEdit: 执行编辑任务
        :param isDelete: 执行删除任务
        :return: 编辑后的list
        """
        # 转换任务id
        recitationId = str(recitationId).zfill(6)
        # 调用工具编辑任务
        self.editRecitationTools.edit(self.list, recitationId, question=question, answer=answer, isEdit=isEdit,
                                      isDelete=isDelete, weight=weight)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{RECITATION_DEBUG} recitation has been edited successful')

    def saveRecitation(self):
        """
        一级子系统的保存任务操作
        :return:
        """
        # 调用工具保存任务
        self.saveRecitationTools.saveFiles(list=self.list)
        # 打印 debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{RECITATION_DEBUG} recitation has been saved successful')

    def searchRecitation(self, recitationId):
        """
        查询任务信息
        :param recitationId: id
        :return:
        """
        # 转换任务id
        recitationId = str(recitationId).zfill(6)
        # 返回当前任务的信息
        for each in self.list:
            if each['recitationId'] == recitationId:
                return each
        pass

    def searchRecitation(self, recitationId):
        """
        查询任务信息
        :param recitationId: id
        :return:
        """
        # 转换任务id
        recitationId = str(recitationId).zfill(6)
        # 返回当前任务的信息
        for each in self.list:
            if each['recitationId'] == recitationId:
                return each
        pass

    def getOneRecitation(self):
        """
        获取一条信息
        :return:
        """
        mapList = []
        pass


if __name__ == '__main__':
    pass
    # m = MissionSystem()
    # f = open('../../data/mission.dat')
    # print(f.read())
