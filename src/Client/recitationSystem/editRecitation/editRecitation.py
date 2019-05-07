# -*- coding:utf-8 -*-

from src.Client.Conf.config import *
from src.Client.recitationSystem.editRecitation.tools import editRecitationList, removeRecitation
from src.Client.SystemTools.SaveFiles import saveFiles


class EditRecitation():
    """
    编辑任务子系统。调用类，任务由被调用者完成。
    """

    def __init__(self, filename='../data/recitation.dat'):
        # 初始化工具
        self.editRecitationListTools = editRecitationList.EditRecitationList()
        self.removeRecitationTools = removeRecitation.RemoveRecitation()
        self.saveRecitationTools = saveFiles.SaveFiles(filename=filename)
        pass

    def edit(self, list, recitationId, question=None, answer=None, isEdit=False, isDelete=False, weight=10):
        """

        :param list: 需要被编辑的列表
        :param recitationId: 任务id
        :param question: 问题
        :param answer: 答案
        :param weight: 权重
        :param isEdit: 执行编辑任务标记
        :param isDelete: 执行删除任务标记
        :return: 编辑后的list
        """
        try:
            # 对不同的编辑命令做出不同的响应
            if isEdit:
                # 调用编辑子系统
                list = self.editRecitationListTools.edit(list=list, recitationId=recitationId, question=question,
                                                         answer=answer, weight=weight)
                self.saveRecitationTools.saveFiles(list)

            if isDelete:
                # 调用删除子系统
                list = self.removeRecitationTools.remove(list=list, recitationId=recitationId)
                self.saveRecitationTools.saveFiles(list)
        except:
            # 打印debug日志
            if DEBUG and MISSION_DEBUG:
                print('{SYS}{W}{RECITATION_DEBUG} can not edit recitation')


# 测试任务编辑系统
if __name__ == '__main__':
    from src.Client.SystemTools.LoadFiles import loadFiles

    l = loadFiles.LoadFiles("F:\python17\pythonPro\MemortAssit\data\mission.dat")
    list = l.loadFiles(missionType='mission')
    print(list)
    print()
    e = EditRecitation('F:\python17\pythonPro\MemortAssit\data\mission.dat')
    # 测试更改完成状态
    # e.edit(list, '000025', isFinish=True)
    # 测试更改
    # e.edit(list, '000025', isEdit=True, bookName='bookTest')
    # 测试删除
    e.edit(list, '000025', isDelete=True)
    print(list)
