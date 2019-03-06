# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.DatabaseSystem.Tools.editUserCodeAndLogTime import EditUserCodeAndLogTime
from src.Server.DatabaseSystem.Tools.saveNewUserCodeToDatabase import SaveNewUserCodeToDataBase


class DatabaseSystem():
    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["MemoryAssist"]
        self.totalCol = mydb["total_user"]
        self.weeklyCol = mydb["weekly_user"]
        self.editTools = EditUserCodeAndLogTime(self.totalCol, self.weeklyCol)
        self.saveTools = SaveNewUserCodeToDataBase(self.totalCol, self.weeklyCol)
        pass

    def newCode(self, userCode, userIp):
        self.saveTools.save(userCode, userIp)

    def editCode(self, userCode, userIp, logTime):
        self.editTools.save(userCode, userIp, logTime)
