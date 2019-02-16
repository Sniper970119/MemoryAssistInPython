# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.MissionSystem import missionSystem
from src.SearchSystem.TranslateTools import translateInWebXml


class SearchSystem():
    """
    搜索子系统。区分搜索的类型，分别调用查词或者任务系统的任务搜索方法。
    """
    def __init__(self, dataFileName='data\mission.dat'):
        # 初始化工具
        self.missionSystemTools = missionSystem.MissionSystem(dataFileName=dataFileName)
        self.translateTools = translateInWebXml.Translate()

    def search(self, words):
        """
        查找单词或者搜索任务id
        :param words: 单词或id
        :return: 单词的翻译信息或者id的任务信息
        """
        result = None
        # 判断是不是单词，来区分单词和任务的区分调用
        if self.isWord(words):
            # 打印debug日志
            if DEBUG and SEARCH_DEBUG:
                print('{SYS}{SEARCH_DEBUG} word translate')
            result = self.translateTools.translate(words)
            # 应对无法完成翻译，翻译模块无法解析返回文本，错误处理返回None作为无法处理信息
            if result is None:
                # 继续向调用者反馈无法翻译的信息，以便向用户做出说明
                return None, True
            return result, True
        else:
            # 打印debug日志
            if DEBUG and SEARCH_DEBUG:
                print('{SYS}{SEARCH_DEBUG} mission search')
            result = self.missionSystemTools.searchMission(words)
            return result, False

    def isWord(self, word):
        """
        判断是否是单词
        :param word: 需要判断的文本
        :return: 是否是单词（所有非纯数字均认为是单词）
        """
        try:
            int(word)
            return False
        except:
            return True


if __name__ == '__main__':
    # print(SearchSystem('F:\python17\pythonPro\MemortAssit\data\mission.dat').isWord('aa'))
    SearchSystem('F:\python17\pythonPro\MemortAssit\data\mission.dat').search('banana')
    pass
