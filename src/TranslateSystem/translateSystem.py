# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.TranslateSystem.Tools import translateInBaidu


class TranslateSystem():
    def __init__(self):
        self.translateInBaiduTools = translateInBaidu.Translate()
        pass

    def translate(self, text):
        result = self.translateInBaiduTools.translate(text)
        return result


if __name__ == '__main__':
    text = 'this is a test'
    res = TranslateSystem().translate(text)
    print(res)
