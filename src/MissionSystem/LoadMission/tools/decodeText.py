# -*- coding:utf-8 -*-
import binascii
import pickle

from src.Conf.config import *


class DecodeText():

    def decodeing(self, data):
        byte_data = binascii.a2b_hex(data)
        list = pickle.loads(byte_data)
        if DEBUG and MISSION_DEBUG:
            print('{MISSION_DEBUG}{DECODE_TEXT} list has been decode successfully')
        return list

