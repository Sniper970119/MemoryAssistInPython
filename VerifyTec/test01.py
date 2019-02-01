# -*- coding:utf-8 -*-

DEBUG = True
# DEBUG = False

import tkinter
from tkinter import ttk
from tkinter import messagebox

# 添加主页面
rootWindow = tkinter.Tk()
rootWindow.title('技术验证01')
rootWindow.geometry('700x500')

# 添加主框架
if DEBUG:
    rootFrame = tkinter.Frame(rootWindow, height=500, width=700, bg='red')
else:
    rootFrame = tkinter.Frame(rootWindow, height=500, width=700)

rootFrame.place(x=0, y=0, anchor='nw')

# 添加消息框架
if DEBUG:
    messageFrame = tkinter.Frame(rootFrame, height=380, width=600, bg='yellow')
else:
    messageFrame = tkinter.Frame(rootFrame, height=380, width=600)

messageFrame.place(x=100, y=50, anchor='nw')

# 添加搜索框架
if DEBUG:
    searchFrame = tkinter.Frame(rootFrame, height=50, width=700, bg='green')
else:
    searchFrame = tkinter.Frame(rootFrame, height=50, width=700)

searchFrame.place(x=0, y=0, anchor='nw')

# 添加预留框架
if DEBUG:
    reserveFrame = tkinter.Frame(rootFrame, height=100, width=700, bg='brown')
else:
    reserveFrame = tkinter.Frame(rootFrame, height=100, width=700)

reserveFrame.place(x=0, y=430, anchor='nw')

# 添加菜单框架
if DEBUG:
    menuFrame = tkinter.Frame(rootFrame, height=380, width=100, bg='purple')
else:
    menuFrame = tkinter.Frame(rootFrame, height=380, width=100)

menuFrame.place(x=0, y=50, anchor='nw')


# 定义鼠标双击事件
def treeviewClick(event):
    isFinish = tkinter.messagebox.askyesno(title='完成任务', message='已完成当前任务')
    if isFinish:
        # for item in tree.selection():
        #     item_text = tree.item(item, "values")
        # tree.selection_remove(tree.selection)
        pass
    if DEBUG:
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print('treeview has been double click at ' + item_text[0])
            print('user select ' + str(isFinish))
    pass


# 在消息框架中添加treeView
tree = ttk.Treeview(messageFrame, columns=['1', '2', '3', '4', '5'], show='headings', height=18)
tree.column('1', width=120, anchor='center')
tree.column('2', width=120, anchor='center')
tree.column('3', width=120, anchor='center')
tree.column('4', width=120, anchor='center')
tree.column('5', width=120, anchor='center')
tree.heading('1', text='任务id')
tree.heading('2', text='书名')
tree.heading('3', text='任务范围')
tree.heading('4', text='任务进度')
tree.heading('5', text='下次任务')
tree.place(x=0, y=0, anchor='nw')
tree.bind("<Double-Button-1>", treeviewClick)

# 向表格中添加测试数据
if DEBUG:
    dataList = []
    for i in range(21):
        # 先封装成字典，方便后期删除
        dir = {
            '任务id': str(i).zfill(4),
            '书名': 'book' + str(i).zfill(2),
            '任务范围': 'mission' + str(i).zfill(2),
            '任务进度': 'state' + str(i).zfill(2),
            '下次任务': 'nextData' + str(i).zfill(2)
        }
        dataList.append(dir)
    for li in dataList:
        # 转换成列表，方便插入treeview
        dataInList = [li['任务id'], li['书名'], li['任务范围'], li['任务进度'], li['下次任务']]
        tree.insert('', 'end', values=dataInList)

rootWindow.mainloop()
