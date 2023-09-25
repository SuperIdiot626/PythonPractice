#2020年12月10日20:19:06

filename = '鬼畜.txt'
with open(filename,'a') as fileobject:
    i=0
    while 1:
        fileobject.write("窝窝头，一块钱四个，嘿嘿！\n")
        i+=1
        if i==5:
            break