# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.MissionSystem.LoadMission import loadMission
from src.MissionSystem.BackupMission import backupMission
from src.MissionSystem.SaveMission import saveMission
from src.MissionSystem.EditMission import editMission
from src.MissionSystem.AddMission import addMission


class MissionSystem():
    def __init__(self, confFileName='F:\python17\pythonPro\MemortAssit\conf\mession.ini',
                 dataFileName='F:\python17\pythonPro\MemortAssit\data\mission.dat',
                 backupFilePath='F:\python17\pythonPro\MemortAssit\data/bkup/mbk/'):
        # if DEBUG and MISSION_DEBUG:
        #     print('mission system start to init')
        self.loadMissionTools = loadMission.LoadMission(filename=dataFileName)
        self.addMissionTools = addMission.AddMission(confFileName=confFileName, dataFileName=dataFileName)
        self.editMissionTools = editMission.EditMission(filename=dataFileName)
        self.saveMissionTools = saveMission.SaveMission(filename=dataFileName)
        self.backupMissionTools = backupMission.BackupMission(fileLimit=7, backupFilePath=backupFilePath,
                                                              missionFileName=dataFileName)
        self.list = self.loadMission()
        self.todayMission = self.findTodayMission()
        # if DEBUG and MISSION_DEBUG:
        # print('mission system finish init')

    def loadMission(self):
        """
        一级子系统的读取任务文件
        :return:
        """
        list = self.loadMissionTools.loadMission()
        if list == None:
            self.backupMissionTools.recover()
        return list

    def findTodayMission(self):
        """
        一级子系统的读取任务文件
        :return:
        """
        todayList = []
        today = datetime.datetime.strptime(time.strftime("%Y-%m-%d", time.localtime()), '%Y-%m-%d').strftime(
            "%Y-%m-%d")
        for each in self.list:
            if each['nextTime'] == today:
                each['isFinish'] = False
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
        self.addMissionTools.addMission(list=self.list, bookName=bookName, missionRange=missionRange,
                                        missionId=missionId,
                                        nextTime=nextTime, state=state, loopTime=loopTime,
                                        isFinish=isFinish)
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
        self.editMissionTools.edit(self.list, missionId, bookName=bookName, missionRange=missionRange,
                                   nextTime=nextTime,
                                   state=state, loopTime=loopTime, isEdit=isEdit, isFinish=isFinish, isDelete=isDelete)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been edited successful')

    def saveMission(self):
        """
        一级子系统的保存任务操作
        :param list:
        :return:
        """
        self.saveMissionTools.saveMission(list=self.list)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been saved successful')

    def backupMission(self):
        """
        一级子系统的文件备份任务
        :param list:
        :return:
        """
        self.backupMissionTools.backup(list=self.list)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{R}{MISSION_DEBUG} mission has been backup successful')

    def searchMission(self, missionId):
        """
        查询任务信息
        :param missionId:
        :return:
        """
        missionId = str(missionId).zfill(6)
        for each in self.list:
            if each['missionId'] == missionId:
                return each
        pass


if __name__ == '__main__':
    m = MissionSystem()
    # f = open('../../data/mission.dat')
    # print(f.read())
