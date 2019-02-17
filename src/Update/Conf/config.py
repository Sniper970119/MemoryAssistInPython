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
# 服务器ip
SERVER_IP = '127.0.0.1'
# 服务器端口
SERVER_FILE_PORT = 9000
SERVER_MES_PORT = 9001



# 调试模式总开关
DEBUG = True
# 版本控制调试开关
VERSION_CONTROL_DEBUG = True


