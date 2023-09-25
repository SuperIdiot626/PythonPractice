#2020年12月10日20:24:53
import os
filename='alice'
os.chdir("D:\Code\Python\源代码文件\源代码文件\chapter_10")


try:
    with open(filename+".txt",encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print("未找到指定文件%s"%filename)
words=contents.split()
length=len(words)
print("book %s has %d words"%(filename,length))
