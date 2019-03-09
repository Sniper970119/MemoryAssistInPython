# -*- coding:utf-8 -*-
from src.Server.Conf.config import *
from src.Server.SystemTools.ConfFileRead import configFileRead
from src.Server.DatabaseSystem.Tools.areaStatistics import AreaStatistics
from src.Server.DatabaseSystem.Tools.returnAllCount import ReturnAllCount
from src.Server.DatabaseSystem.Tools.returnAllLog import ReturnAllLog


class SendEmail():
    def __init__(self):
        self.areaTools = AreaStatistics()
        self.allCountTools = ReturnAllCount()
        self.allLogTools = ReturnAllLog()
        pass

    def send(self):
        print("need to send email")
        # 获取邮件需要的信息
        weeklyArea, totalArea = self.areaTools.statistics()
        weeklyAllCount, totalAllCount = self.allCountTools.statistics()
        weeklyLogCount, totalLogCount = self.allLogTools.statistics()
        # 发送邮件准备
        msg_from = 'MemoryAssist@sniper97.cn'  # 发送方邮箱
        passwd = 'ysqmxpfdkxhsbigd'  # 填入发送方邮箱的授权码
        msg_to = 'zhaoyu@sniper97.cn'  # 收件人邮箱

        subject = "MemoryAssist 每周使用报告"  # 主题
        content = str("本周登录次数：" + str(weeklyLogCount) + "\n本周用户数量：" + str(weeklyAllCount) + "\n\n总计登录次数：" + str(
            totalLogCount) + "\n总计用户数量：" + str(totalAllCount) + "\n\n\n本周用户地区分布：" +
                      json.dumps(weeklyArea).encode('utf-8').decode('unicode_escape') + "\n\n总计地区分布：" + str(
            json.dumps(totalArea)).encode('utf-8').decode('unicode_escape'))
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        # 发送email
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print('email send')
        except s.SMTPException, e:
            # 打开错误日志文件
            wrongFile = open('data/wrongMessage.dat', 'a+')
            # 获取当前时间
            currentTime = str(datetime.datetime.strptime(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()),
                                                         '%Y-%m-%d-%H-%M-%S'))
            # 生成报错的错误信息
            wrongMessage = {
                '|currentTime': currentTime,
                '|file': 'DatabaseSystem-saveNewUserCodeToDatabase',
                '|wrongMessage': msg,
            }
            # 存入文件
            wrongFile.write(str(wrongMessage))
            # 增加换行符
            wrongFile.write('\n')
            wrongFile.close()
        pass
