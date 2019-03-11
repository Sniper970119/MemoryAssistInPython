# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.MessageTransferSystem.VersionControlSystem import versionControl
from src.Server.MessageReportSystem.messageReportSystem import MessageReportSystem

import os

# 主界面
if __name__ == '__main__':
    versionControl.VersionControl()
    threading.Thread(target=MessageReportSystem().run()).start()
    # schedule.every().monday.at("00:00").do(MessageReportSystem().run())
    # while True: