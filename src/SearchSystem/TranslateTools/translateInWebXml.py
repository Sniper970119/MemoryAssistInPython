# -*- coding:utf-8 -*-
from src.Conf.config import *


class Translate():
    def translate(self, word):
        translateURL = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/Translator?wordKey=' + word
        r = requests.get(translateURL)
        text = r.text
        if self.isChinese(word):
            message = self.handleCNRequest(text)
        else:
            message = self.handleENRequest(text)
        return message

    def handleCNRequest(self, text):

        wordDir = {
            'word': re.findall('<WordKey>(.*?)</WordKey>', text)[0],
            'pron': '[' + re.findall('<Pron>(.*?)</Pron>', text)[0] + ']',
            'translation': re.findall('<Translation>(.*?)</Translation>', text)[0],
            'sentenceOneOrig': re.findall('<Orig>(.*?)</Orig>', text)[0],
            'sentenceOneTrans': re.findall('<Trans>(.*?)</Trans>', text)[0],
            'sentenceTwoOrig': re.findall('<Orig>(.*?)</Orig>', text)[1],
            'sentenceTwoTrans': re.findall('<Trans>(.*?)</Trans>', text)[1],
        }
        if DEBUG and SEARCH_DEBUG:
            print('{SYS}{SEARCH_DEBUG} translate CN into EN, result is '+ wordDir['translation'])
        return wordDir

    def handleENRequest(self, text):
        wordDir = {
            'word': re.findall('<WordKey>(.*?)</WordKey>', text)[0],
            'pron': '[' + re.findall('<Pron>(.*?)</Pron>', text)[0] + ']',
            'translation': re.findall('<Translation>(.*?)</Translation>', text)[0],
            'sentenceOneOrig': re.findall('<Orig>(.*?)</Orig>', text)[0],
            'sentenceOneTrans': re.findall('<Trans>(.*?)</Trans>', text)[0],
            'sentenceTwoOrig': re.findall('<Orig>(.*?)</Orig>', text)[1],
            'sentenceTwoTrans': re.findall('<Trans>(.*?)</Trans>', text)[1],
        }
        if DEBUG and SEARCH_DEBUG:
            print('{SYS}{SEARCH_DEBUG} translate EN into CN, result is '+ wordDir['translation'])
        return wordDir

    def isChinese(self, word):
        for ch in word.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


if __name__ == '__main__':
    # print(Translate().isChinese('aa'))
    # print(Translate().isChinese('火车'))
    Translate().translate('train')
    pass
