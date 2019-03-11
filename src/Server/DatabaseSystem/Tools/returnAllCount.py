# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class ReturnAllCount():
    """
    返回所有的访问次数
    """
    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["MemoryAssist"]
        self.totalCol = mydb["total_user"]
        self.weeklyCol = mydb["weekly_user"]

    def statistics(self):
        """
        返回所有的访问次数
        :return:
        """
        return self.weeklyCol.count(), self.totalCol.count()
