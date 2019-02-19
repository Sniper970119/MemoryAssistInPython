# -*- coding:utf-8 -*-
import zipfile
import shutil
import os


def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "_files/")
    zip_file.close()
    moveFile()


def moveFile():
    for filename in os.listdir('./testPck1.zip_files/testPck1/'):
        print(filename)
        try:
            os.remove('./testPck/' + filename)
        except:
            shutil.rmtree('./testPck/'+filename)
            pass
        shutil.move('./testPck1.zip_files/testPck1/' + filename, './testPck/')
    shutil.rmtree('./testPck1.zip_files')


if __name__ == '__main__':
    un_zip('testPck1.zip')
