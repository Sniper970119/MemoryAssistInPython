# -*- coding:utf-8 -*-


class Misson():
    def __init__(self, missionId, bookName, missionRange, nextTime, state=1, loopTime=5, isFinish=False):
        """
        :param missionId: 任务id
        :param bookName: 任务书名
        :param missionRange: 任务范围
        :param nextTime: 下次复习时间
        :param state: 当前任务状态（默认为新）
        :param loopTime: 当状态码为7时循环出现次数（默认五次）
        :param isFinish: 当前任务是否完成（默认未完成）
        """
        # 定义几种任务状态的常量，分别为，不再提示、新任务、一天后重复、两天后重复···和更多（15天）
        self.NEVER = 0
        self.NEW_MISSION = 1
        self.ONE_DAY = 2
        self.TWO_DAY = 3
        self.FOUR_DAY = 4
        self.SEVEN_DAY = 5
        self.FIFTH_DAY = 6
        self.MORE = 7
        # 变量赋值
        self.missionId = missionId
        self.bookName = bookName
        self.missionRange = missionRange
        self.nextTime = nextTime
        self.state = state
        self.loopTime = loopTime
        self.isFinish = isFinish

        pass
