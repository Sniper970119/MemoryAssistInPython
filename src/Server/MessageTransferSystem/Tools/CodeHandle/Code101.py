# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead


class Code101():
    def __init__(self):
        pass

    def respond(self, connect):
        """
        响应代码101
        :param connect: 与客户端的连接
        :return:
        """
        # 生成随机的32位识别码
        code = ''.join(random.sample(string.ascii_letters + string.digits, 32))
        # 将随机生成码保存到数据库中
        # -------------------------------------------------------------------------

        # 发送随机识别码
        connect.send(code.encode('utf-8'))
