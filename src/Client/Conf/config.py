# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk
from tkinter import messagebox
import ConfigParser
import time
import datetime
import os
import threading
import requests
import re
import win32clipboard
import win32con
import socket
import struct
"""
该类负责导入包、debug开关
"""

# 服务器端口
SERVER_FILE_PORT = 9000
SERVER_MES_PORT = 9001


VERSION = 1.0



# 调试模式总开关
DEBUG = True
# GUI部分调试开关
VIEW_DEBUG = True
# 任务系统调试开关
MISSION_DEBUG = True
# 搜索系统调试开关
SEARCH_DEBUG = True
# 系统工具调试开关
SYSTEM_TOOLS_DEBUG = True
# 版本控制调试开关
VERSION_CONTROL_DEBUG = True


if DEBUG:
    # 服务器ip
    SERVER_IP = '127.0.0.1'
else:
    # 服务器ip
    SERVER_IP = 'memoryassist.sniper97.cn'

