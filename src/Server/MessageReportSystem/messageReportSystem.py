# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail

class MessageReportSystem():
    def __init__(self):

        pass

    def run(self):
        """
        定时任务开启，需要多线程执行。定时每周周一零点发送任务信息
        :return:
        """
        # 任务调度，每周周一定时任务
        schedule.every().monday.at("00:00").do(SendEmail().send)
        # schedule.every().day.at("10:13").do(SendEmail().send)
        while True:
            # 启动服务
            schedule.run_pending()
            # 休眠一分钟
            time.sleep(60)
            # time.sleep(1)
        pass

