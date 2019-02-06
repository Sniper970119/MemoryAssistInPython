import os

path = 'F:\python17\pythonPro\MemortAssit\data/bkup'
files = os.listdir(path)
minFileName = None
minFileTime = 0
for file in files:
    if minFileTime == 0:
        minFileTime = os.path.getctime(path + '/' + file)
        minFileName = file
    else:
        if minFileTime > os.path.getctime(path + '/' + file):
            minFileTime = os.path.getctime(path + '/' + file)
            minFileName = file
print(minFileName)

