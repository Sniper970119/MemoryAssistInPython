# -*- coding:utf-8 -*-
from src.Conf.config import *

from src.MissionSystem import missionSystem
from src.SearchSystem.TranslateTools import translateInBaidu


class SearchSystem():
    def __init__(self, dataFileName='data\mission.dat'):
        self.missionSystemTools = missionSystem.MissionSystem(dataFileName=dataFileName)
        self.translateTools = translateInBaidu.Translate()
        pass

    def search(self, words):
        result = None
        if self.isWord(words):
            print('is word')
            result = self.translateTools.translate(words)
            print(type(result))
            print(result)

        else:
            print('is mission')
            result = self.missionSystemTools.searchMission(words)
            print(type(result))
        pass

    def isWord(self, word):
        try:
            int(word)
            return False
        except:
            return True
        # print(word.isdigit())
        # return word.isdigit()


if __name__ == '__main__':
    # print(SearchSystem('F:\python17\pythonPro\MemortAssit\data\mission.dat').isWord('aa'))
    SearchSystem('F:\python17\pythonPro\MemortAssit\data\mission.dat').search('banana')
    pass
