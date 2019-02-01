# -*- coding:utf-8 -*-

DEBUG = True
# DEBUG = False

import tkinter
from tkinter import ttk
from tkinter import messagebox

# 添加主页面
rootWindow = tkinter.Tk()
rootWindow.title('技术验证01')
rootWindow.iconbitmap('../images/icon.ico')
screenWidth = rootWindow.winfo_screenwidth()
screenHeight = rootWindow.winfo_screenheight()
rootWindow.geometry('700x500+' + str(int((screenWidth - 700) / 2)) + '+' + str(int((screenHeight - 500) / 2)))
rootWindow.resizable(width=False, height=False)

# 添加主框架
if DEBUG:
    rootFrame = tkinter.Frame(rootWindow, height=500, width=700, bg='red')
else:
    rootFrame = tkinter.Frame(rootWindow, height=500, width=700)

rootFrame.place(x=0, y=0, anchor='nw')

# 添加顶部框架
if DEBUG:
    topFrame = tkinter.Frame(rootFrame, height=50, width=700, bg='lightPink')
else:
    topFrame = tkinter.Frame(rootFrame, height=50, width=700)

topFrame.place(x=0, y=0, anchor='nw')

# 添加预留框架
if DEBUG:
    reserveFrame = tkinter.Frame(rootFrame, height=100, width=700, bg='hotpink')
else:
    reserveFrame = tkinter.Frame(rootFrame, height=100, width=700)

reserveFrame.place(x=0, y=430, anchor='nw')

# 定义tab标签页
tab = ttk.Notebook(rootFrame, height=350, width=700)

tab.place(x=0, y=50, anchor='nw')

# 定义tab 中的主框架
if DEBUG:
    firstTabFrame = tkinter.Frame(tab, height=350, width=700, bg='Thistle')
else:
    firstTabFrame = tkinter.Frame(tab, height=350, width=700)

firstTabFrame.place(x=0, y=30, anchor='nw')

# 添加消息框架
if DEBUG:
    messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600, bg='yellow')
else:
    messageFrame = tkinter.Frame(firstTabFrame, height=350, width=600)

messageFrame.place(x=0, y=00, anchor='nw')

# 添加菜单框架
if DEBUG:
    menuFrame = tkinter.Frame(firstTabFrame, height=350, width=150, bg='pink')
else:
    menuFrame = tkinter.Frame(firstTabFrame, height=350, width=150)

menuFrame.place(x=550, y=00, anchor='nw')

# 添加翻译tab
secondTabFrame = tkinter.Frame(tab)
secondTabFrame.place(x=0, y=0, anchor='nw')

# 添加翻译框架
if DEBUG:
    translateFrame = tkinter.Frame(secondTabFrame, height=350, width=750, bg='plum')
else:
    translateFrame = tkinter.Frame(secondTabFrame, height=350, width=750)

translateFrame.place(x=0, y=0, anchor='nw')

# 将tab框架添加到tab中
tab.add(firstTabFrame, text='我的计划')
tab.add(secondTabFrame, text='我要查词')


# 定义鼠标双击事件
def treeviewClick(event):
    """
    定义鼠标在treeview上的双击事件
    :param event:
    :return:
    """
    if DEBUG:
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print('treeview has been double click at ' + item_text[0])
    isFinish = tkinter.messagebox.askyesno(title='完成任务', message='已完成当前任务')
    if isFinish:
        for item in tree.selection():
            item_text = tree.item(item, "values")
            removeData(item_text[0])
        pass
    if DEBUG:
        print('user select ' + str(isFinish))
    pass


# 在消息框架中添加treeView
tree = ttk.Treeview(messageFrame, columns=['1', '2', '3', '4', '5'], show='headings', height=18)
tree.column('1', width=110, anchor='center')
tree.column('2', width=110, anchor='center')
tree.column('3', width=110, anchor='center')
tree.column('4', width=110, anchor='center')
tree.column('5', width=110, anchor='center')
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
    for i in range(1, 21):
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


def removeData(id):
    """
    从treeview中移除id
    :param id: 需要被移除的id
    :return:
    """
    if DEBUG:
        print('current delete id is ' + id)
    # 先删除所有点
    x = tree.get_children()
    for item in x:
        tree.delete(item)
    for each in dataList:
        if each['任务id'] != id:
            # 转换成列表，方便插入treeview
            dataInList = [each['任务id'], each['书名'], each['任务范围'], each['任务进度'], each['下次任务']]
            tree.insert('', 'end', values=dataInList)


# 添加搜索栏
searchBox = tkinter.Entry(topFrame, font=('Arial', 12), width=35, bd=5, relief='flat')
searchBox.place(x=130, y=10, anchor='nw')


# 定义搜索按钮事件
def searchButtonHadle():
    searchText = searchBox.get()
    if DEBUG:
        print('search button has been click,and the search text is ' + searchText)
    pass


# 添加搜索按钮
searchImage = tkinter.PhotoImage(file="../images/search.gif")
searchButton = tkinter.Button(topFrame, image=searchImage, command=searchButtonHadle)
searchButton.place(x=470, y=8.5, anchor='nw')

rootWindow.mainloop()
