# -*- coding:utf-8 -*-
import socket
import datetime
import time
from tkinter import messagebox
# import configparser as ConfigParser
import ConfigParser
import struct
import zipfile
import shutil
import os

# SERVER_IP = '140.143.147.128'
# SERVER_IP = '127.0.0.1'
SERVER_FILE_PORT = 9000
SERVER_MES_PORT = 9001

DEBUG = False
SYSTEM_TOOLS_DEBUG = True
VERSION_CONTROL_DEBUG = True

if DEBUG:
    # 服务器ip
    SERVER_IP = '127.0.0.1'
else:
    # 服务器ip
    SERVER_IP = 'memoryassist.sniper97.cn'
