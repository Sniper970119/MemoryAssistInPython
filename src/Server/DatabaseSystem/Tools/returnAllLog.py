# -*- coding:utf-8 -*-
from src.Server.Conf.config import *

class ReturnAllLog():
    """
    计算所有登录次数
    """
    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["MemoryAssist"]
        self.totalCol = mydb["total_user"]
        self.weeklyCol = mydb["weekly_user"]
        pass

    def compute(self):
        """
        计算所有登录次数
        :return: 分别返回周登录次数和总登录次数
        """
        weekLogCount = 0
        totalLogCount = 0
        for each in self.weeklyCol.find():
            weekLogCount = weekLogCount + each['weekly_time']
            pass

        for each in self.totalCol.find():
            totalLogCount = totalLogCount + each['total_time']
            pass

        return weekLogCount, totalLogCount