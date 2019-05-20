# -*- coding:utf-8 -*-
from src.Client.View.MainFrame import mainFrame
from src.Client.View.MainFrame.SearchAndSettingFrame.ShowSettingTools.showEdit import ShowEdit
from src.Client.recitationSystem.recitationSystem import RecitationSystem
from src.Server.MessageReportSystem.Tools.sendEmail import SendEmail
from src.Server.SystemTools.ConfFileRead import configFileRead

if __name__ == '__main__':
    m = RecitationSystem()
    # 添加
    # m.addRecitation('question1', 'answer1', weight=10)
    # m.addRecitation('question2', 'answer2', weight=20)
    # 获取一条
    # print(m.loadRecitation())
    # m.editRecitation(recitationId='000001',
    #                  question='question1',
    #                  answer='运行程序，超出Label的那部分文本被截断了，常用的方法是：使用自动换行功能，及当文本长度大于控件的宽度时，文本应该换到下一行显示，Tk不会自动处理，但提供了属性： wraplength： 指定多少单位后开始换行 justify: 指定多行的对齐方式 ahchor： 指定文本(text)或图像(bitmap/image)在Label中的显示位',isEdit=True)
    # print(m.getOneRecitation())
    print(type(configFileRead.ConfigFileRead().readFile('EMAIL', 'email_code'))
)