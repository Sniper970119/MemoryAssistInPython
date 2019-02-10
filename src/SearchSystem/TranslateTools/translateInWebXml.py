# -*- coding:utf-8 -*-
from src.Conf.config import *


class Translate():
    def translate(self, word):
        """
        翻译单词（返回详细的单词翻译）
        :param word: 需要被翻译的文本（英汉均可）
        :return:
        """
        translateURL = 'http://fy.webxml.com.cn/webservices/EnglishChinese.asmx/Translator?wordKey=' + word
        r = requests.get(translateURL)
        text = r.text
        # 判断翻译类型，调用不同的解析方案
        if self.isChinese(word):
            message = self.handleCNRequest(text)
        else:
            message = self.handleENRequest(text)
        return message

    def handleCNRequest(self, text):
        """
        处理中文的翻译响应
        :param text: 响应
        :return: 解析后生成字典
        """
        wordDir = {
            'word': re.findall('<WordKey>(.*?)</WordKey>', text)[0],
            'pron': '[' + re.findall('<Pron>(.*?)</Pron>', text)[0] + ']',
            'translation': re.findall('<Translation>(.*?)</Translation>', text)[0],
            'sentenceOneOrig': re.findall('<Orig>(.*?)</Orig>', text)[0],
            'sentenceOneTrans': re.findall('<Trans>(.*?)</Trans>', text)[0],
            'sentenceTwoOrig': re.findall('<Orig>(.*?)</Orig>', text)[1],
            'sentenceTwoTrans': re.findall('<Trans>(.*?)</Trans>', text)[1],
        }
        # 打印debug日志
        if DEBUG and SEARCH_DEBUG:
            print('{SYS}{SEARCH_DEBUG} translate CN into EN, result is ' + wordDir['translation'])
        return wordDir

    def handleENRequest(self, text):
        """
        处理英文的翻译响应
        :param text: 响应
        :return: 解析后生成字典
        """
        wordDir = {
            'word': re.findall('<WordKey>(.*?)</WordKey>', text)[0],
            'pron': '[' + re.findall('<Pron>(.*?)</Pron>', text)[0] + ']',
            'translation': re.findall('<Translation>(.*?)</Translation>', text)[0],
            'sentenceOneOrig': re.findall('<Orig>(.*?)</Orig>', text)[0],
            'sentenceOneTrans': re.findall('<Trans>(.*?)</Trans>', text)[0],
            'sentenceTwoOrig': re.findall('<Orig>(.*?)</Orig>', text)[1],
            'sentenceTwoTrans': re.findall('<Trans>(.*?)</Trans>', text)[1],
        }
        # 打印debug日志
        if DEBUG and SEARCH_DEBUG:
            print('{SYS}{SEARCH_DEBUG} translate EN into CN, result is ' + wordDir['translation'])
        return wordDir

    def isChinese(self, word):
        """
        判断是否是中文
        :param word: 需要被判断的字符
        :return: 是否是中文
        """
        for ch in word.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


if __name__ == '__main__':
    # print(Translate().isChinese('aa'))
    # print(Translate().isChinese('火车'))
    Translate().translate('train')
    pass
