#coding=utf-8

import shutil
import os
import sys
from yqproject.settings import *

from os.path import walk, join, normpath

#这个是完整的文件夹
PathA = "F:FullData"
#这个是缺文件的文件夹
PathB = "F:IncomplData"

#这个是目标文件夹
PathC = "F:DiffData"

#============================================================
#这个函数是用来递归处理PathA，对PathA里的每个文件和文件夹在PathB中找是否有对应的文件或文件夹
#若找不到，则在PathC中创建目录并拷贝文件
#拷贝文件时使用了shutil模块的copy2函数，以保留文件原来的创建时间和最后更新时间
def visit(arg, dirname, names):
#把目录打印出来，以监视进度
    print dirname

    #得到路径名后，把前面的主路径名去掉
    dir=dirname.replace(PathA,"")

    dirnameB = os.path.join(PathB,dir)
    dirnameC = os.path.join(PathC,dir)

    if os.path.isdir(dirnameB): #若PathB里存在对应的文件夹，再逐个文件判断是否存在
        for file in names:
            if os.path.isfile(os.path.join(dirname,file)) and not os.path.isfile(os.path.join(dirnameB,file)):
                if not os.path.isdir(dirnameC):
                    os.system("mkdir %s"%(dirnameC))
                    shutil.copy2(os.path.join(dirname,file), os.path.join(dirnameC,file))
                elif os.path.isdir(os.path.join(dirname,file)) and not os.path.isdir(os.path.join(dirnameB,file)):
                    if not os.path.isdir(os.path.join(dirnameC,file)):
                        os.system("mkdir %s"%(os.path.join(dirnameC,file)))
    else:
    #若pathB里不存在对应的文件夹，则在pathC里创建对应的文件夹并拷贝文件
        if not os.path.isdir(dirnameC):
            os.system("mkdir %s"%(dirnameC))

    for file in names:
        shutil.copy2(os.path.join(dirname,file), os.path.join(dirnameC,file))

# if __name__ == '__main__':
#     a = os.walk('/home/monkeys/PycharmProjects/untitled')
#     for i in a:
#         if i[1] == []:
#             print i

def copy_file():
    dir1 = DOC_DIR + '/topic'  #yqproject/documents/topic
    dir2 = BASE_DIR+'/static/sna' #yqproject/static/sna
    temp_sna = '/home/monkeys/PycharmProjects/temp_sna/sna'
    temp_txt = '/home/monkeys/PycharmProjects/temp_txt/topic'
    # if not os.path.isdir(dir2):
    #     os.makedirs(dir2)
    # if not os.path.isdir(temp_txt):
    #     os.makedirs(temp_txt)
    # else:
    #     pass
    # if not os.path.isdir(temp_sna):
    #     os.makedirs(temp_sna)
    # else:
    #     pass
    roots = os.walk(dir1)
    for dir in roots:

        if dir[2] !=[] and dir[1] == []: #到达最底层
            print 'dir',dir #('dir', ['child dir'], [files])
            for j in dir[2]: #j is file
                print 'file', j
                dst = dir[0].replace('yqproject/documents','ggg') #判重目录
                # print 'dst',dst
                if not os.path.isdir(dst):
                    os.makedirs(dst)
                temp1 = dir[0].replace('yqproject/documents','temp_txt') #传输目录
                # print 'txt',temp1
                if not os.path.isdir(temp1):
                    os.makedirs(temp1)


                if os.path.isfile(os.path.join(dst,j)):
                    pass
                else:
                   # print os.path.join(dst)
                   try:
                       shutil.copy2(os.path.join(dir[0],j),os.path.join(dst,j)) #方便下次判重
                       shutil.copy2(os.path.join(dir[0],j),os.path.join(temp1,j)) #txt
                   except IOError:
                       print 'txt lost'


            temp2 = dir[0].replace('yqproject/documents/topic','temp_sna/sna') #传输目录
            print 'sna',temp2
            if not os.path.isdir(temp2):
                os.makedirs(temp2)
            try:
                shutil.copy2(os.path.join(dir[0].replace('documents','static/sna'),'SNA.png'),os.path.join(temp2,'SNA.png')) #sna
            except IOError:
                print 'sna lost'
    # os.system('scp -r /home/monkeys/PycharmProjects/temp_txt/topic root@42.96.134.205:/root/yuqing/test')
    os.system('scp -r /home/monkeys/PycharmProjects/temp_txt/topic root@42.96.134.205:/root/yuqing/yqproject/documents')
    os.system('scp -r /home/monkeys/PycharmProjects/yqproject/static/sna root@42.96.134.205:/root/yuqing/yqproject/static')
    try:
        shutil.rmtree(temp_sna)
        shutil.rmtree(temp_txt)
    except:
        print 'empty topic file!!'

# copy_file()
# shutil.copy2('/home/monkeys/py.sh','/home/monkeys/ppp.txt')
# os.system('scp -r /home/monkeys/PycharmProjects/temp_txt/topic root@42.96.134.205:/root/yuqing/test')