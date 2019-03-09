# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail

class MessageReportSystem():
    def __init__(self):

        pass

    def run(self):
        print('run')
        schedule.every().monday.at("00:00").do(SendEmail().send())
        schedule.every().at("22:58").do(SendEmail().send())
        while True:
            # 启动服务
            schedule.run_pending()
            # 休眠一小时
            time.sleep(1)
            # time.sleep(3600)
        pass


    def timeHandle(self):
        pass