# -*- coding:utf-8 -*-
import socket
import datetime
import time
import os
import struct
import threading
import ConfigParser
import random
import string
import pymongo

SERVER_IP = 'localhost'

# 调试模式总开关
DEBUG = True
#
VERSION_CONTROL_DEBUG = True

SYSTEM_TOOLS_DEBUG = True