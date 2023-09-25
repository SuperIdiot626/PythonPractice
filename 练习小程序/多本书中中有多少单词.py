#2020年12月10日20:24:53
import os
filenames=['alice','little_women','moby_dick','lichking']
os.chdir("D:\Code\Python\源代码文件\源代码文件\chapter_10")

def counting_words(filename):
    try:
        with open(filename+".txt",encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        print("未找到%s这本书"%filename)
    else:
        words=contents.split()
        length=len(words)
        print("book %s has %d words"%(filename,length))

for i in filenames:
    counting_words(i)