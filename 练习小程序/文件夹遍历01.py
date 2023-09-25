import os

data=[]
temp=[]

def get_filelist(dir):
    #a=os.getcwd()
    #print(a)
    for home, dirs, files in os.walk(dir):
        if home == targetdir:
            continue
        #print(type(home))
        print(home)
        
        #print(dirs)
        #print(files)
        
        print("#######dir list#######")
        print(type(dirs))
        for dir in dirs:                  #dirs中保存着该目录下的文件夹名
            print(dir)                    #依次输出该目录下的各个子目录（文件夹）名称
        print("#######dir list#######")

        print("#######file list#######")
        for filename in files:
            print(filename)
            fullname = os.path.join(home, filename)
            print(fullname)
        print("#######file list#######")

if __name__ == "__main__":
    #targetdir=input("请输入目标路径：")
    targetdir="D:\Code\Python\练习小程序\数据"
    get_filelist(targetdir)

    #print(type(os.walk(dir)))