# -*- coding:utf-8 -*-
import binascii
import pickle

from src.Conf.config import *



class EncodeText():

    def encodeing(self, data):
        """
        将列表加密
        :param data: 需要加密的列表
        :return: 加密后的结果
        """
        # 首先将列表序列化
        byte_data = pickle.dumps(data)
        # 进制转换加密
        encodeText = binascii.b2a_hex(byte_data)
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} list has been encode successfully')
        return encodeText
