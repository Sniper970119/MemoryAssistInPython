# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.TranslateSystem.Tools import translateInBaidu


class TranslateSystem():
    def __init__(self):
        # 初始化工具
        self.translateInBaiduTools = translateInBaidu.Translate()
        pass

    def translate(self, text):
        """
        翻译一级子系统
        :param text:
        :return:
        """
        result = self.translateInBaiduTools.translate(text)
        return result


if __name__ == '__main__':
    text = 'this is a test'
    res = TranslateSystem().translate(text)
    print(res)
