# -*- coding:utf-8 -*-
from src.Update.Conf.config import *

class UnZipFile():
    def __init__(self, file_name):
        self.fileName = file_name
        pass

    def un_zip(self):
        """
        解压文件
        :return:
        """
        zip_file = zipfile.ZipFile(self.fileName)
        if os.path.isdir(self.fileName + "_files"):
            pass
        else:
            os.mkdir(self.fileName + "_files")
        for names in zip_file.namelist():
            zip_file.extract(names, self.fileName + "_files/")
        zip_file.close()
        self.moveFile()

    def moveFile(self):
        """
        移动文件，将解压后的更新文件移动出来并删除
        :return:
        """
        for filename in os.listdir('./update.zip_files/update/'):
            try:
                os.remove('./' + filename)
            except Exception, e:
                try:
                    shutil.rmtree('./' + filename)
                except Exception, e:
                    pass
                pass
            shutil.move('./update.zip_files/update/' + filename, './')
        # 对多余的文件进行删除
        shutil.rmtree('./update.zip_files')
        os.remove('./' + self.fileName)




if __name__ == '__main__':
    pass
