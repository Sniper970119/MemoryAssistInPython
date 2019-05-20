# -*- coding:utf-8 -*-
from src.Client.Conf.config import *

from src.Client.SystemTools.LoadFiles import loadFiles
from src.Client.MissionSystem.BackupMission import backupMission
from src.Client.SystemTools.SaveFiles import saveFiles
from src.Client.MissionSystem.EditMission import editMission
from src.Client.MissionSystem.AddMission import addMission


class MissionSystem():
    """
    任务系统，一级子系统。对外提供任务系统的各个功能。
    """

    def __init__(self, confFileName='conf\mission.ini',
                 dataFileName='data\mission.dat',
                 backupFilePath='data/bkup/mbk/'):
        # 初始化工具
        self.loadMissionTools = loadFiles.LoadFiles(filename=dataFileName)
        self.addMissionTools = addMission.AddMission(confFileName=confFileName, dataFileName=dataFileName)
        self.editMissionTools = editMission.EditMission(filename=dataFileName)
        self.saveMissionTools = saveFiles.SaveFiles(filename=dataFileName)
        self.backupMissionTools = backupMission.BackupMission(fileLimit=7, backupFilePath=backupFilePath,
                                                              missionFileName=dataFileName)
        self.list = self.loadMission()
        self.todayMission = self.findTodayMission()

    def loadMission(self):
        """
        一级子系统的读取任务文件
        :return:
        """
        # 读取任务文件
        list = self.loadMissionTools.loadFiles(missionType='mission')
        # 如果返回为None，即无法读取正确的配置信息
        if list == None:
            # 使用备份文件恢复数据
            self.backupMissionTools.recover()
        return list

    def findTodayMission(self):
        """
        一级子系统的读取任务文件，返回今天应该完成的任务
        :return:
        """
        # 从文件中读取任务
        self.list = self.loadMission()
        # 今日任务列表
        todayList = []
        today = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d')
        # 将下次任务日期为今天（或更早）的任务取出
        for each in self.list:
            missionTime = datetime.datetime.strptime(each['nextTime'], "%Y-%m-%d")
            if missionTime <= today:
                todayList.append(each)
        return todayList

    def addMission(self, bookName, missionRange, missionId=None, nextTime=None, state=1, loopTime=5,
                   isFinish=False):
        """
        一级子系统的添加任务操作
        :param list:  目标list
        :param missionId: 任务id（string
        :param bookName: 书名
        :param missionRange: 任务范围
        :param nextTime: 下次任务时间
        :param state: 任务状态
        :param loopTime: 剩余迭代次数
        :param isFinish: 任务是否完成
        :return: 添加后的list
        """
        # 转换任务id
        if missionId is not None:
            missionId = str(missionId).zfill(6)
        # 调用增加任务工具
        self.addMissionTools.addMission(list=self.list, bookName=bookName, missionRange=missionRange,
                                        missionId=missionId,
                                        nextTime=nextTime, state=state, loopTime=loopTime,
                                        isFinish=isFinish)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been added successful')

    def editMission(self, missionId, bookName=None, missionRange=None, nextTime=None, state=None, loopTime=None,
                    isEdit=False, isFinish=False, isDelete=False):
        """
        一级子系统的编辑任务操作
        :param list: 需要被编辑的列表
        :param missionId: 任务id
        :param bookName: 书名
        :param missionRange: 任务范围
        :param nextTime: 下次时间
        :param state: 任务状态
        :param loopTime: 迭代次数
        :param isEdit: 执行编辑任务
        :param isFinish: 执行完成任务
        :param isDelete: 执行删除任务
        :return: 编辑后的list
        """
        # 转换任务id
        missionId = str(missionId).zfill(6)
        # 调用工具编辑任务
        self.editMissionTools.edit(self.list, missionId, bookName=bookName, missionRange=missionRange,
                                   nextTime=nextTime,
                                   state=state, loopTime=loopTime, isEdit=isEdit, isFinish=isFinish, isDelete=isDelete)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been edited successful')

    def saveMission(self):
        """
        一级子系统的保存任务操作
        :param list:
        :return:
        """
        # 调用工具保存任务
        self.saveMissionTools.saveFiles(list=self.list)
        # 打印 debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been saved successful')

    def backupMission(self):
        """
        一级子系统的文件备份任务
        :param list:
        :return:
        """
        # 调用工具备份
        self.backupMissionTools.backup(list=self.list)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been backup successful')

    def searchMission(self, missionId):
        """
        查询任务信息
        :param missionId:
        :return:
        """
        # 转换任务id
        missionId = str(missionId).zfill(6)
        # 返回当前任务的信息
        for each in self.list:
            if each['missionId'] == missionId:
                return each
        pass


if __name__ == '__main__':
    m = MissionSystem()
    # f = open('../../data/mission.dat')
    # print(f.read())
