# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class AreaStatistics():
    """
    删除每周数据的数据库
    """

    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        mydb = myclient["MemoryAssist"]
        self.weeklyCol = mydb["weekly_user"]
        pass

    def handle(self):
        """
        删除每周数据的数据库
        :return:
        """
        # 删除数据库中的所有文档
        self.weeklyCol.delete_many({})
