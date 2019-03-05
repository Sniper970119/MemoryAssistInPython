# -*- coding:utf-8 -*-
from src.Server.Conf.config import *


class SaveNewUserCodeToDataBase():
    def __init__(self):
        myclient = pymongo.MongoClient("localhost:27017")
        self.mydb = myclient["runoobdb"]
        pass

    def save(self, code):
        pass
