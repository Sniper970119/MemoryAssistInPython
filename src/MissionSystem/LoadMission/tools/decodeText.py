# -*- coding:utf-8 -*-
import binascii
import pickle

from src.Conf.config import *


class DecodeText():

    def decodeing(self, data):
        """
        解密
        :param data: 需要被解密的数据
        :return: 解密后的列表
        """
        # 将文本转换进制
        byte_data = binascii.a2b_hex(data)
        # 反序列化
        list = pickle.loads(byte_data)
        # 打印debug日志
        if DEBUG and MISSION_DEBUG:
            print('{SYS}{MISSION_DEBUG} list has been decode successfully')
        return list

