def main():
    file_location,dire=reference_input()
    states=states_readin(file_location)
    i=0
    while 1:
        dirname=states[i][0]
        state=states[i][1:]
        if i==0:
            stringPart1,stringPart2=fileread(dire,dirname)
            if stringPart1=='':
                print('model file error')
                break
        try:
            file=open(dire+'\\'+dirname+'\\mcfd.inp','w')
        except:
            print(dire+'\\'+dirname+' not found')
            break
        filewriteParts(file,stringPart1)
        file.write('values ')
        for j in state:
            file.write(j+' ')
        file.write('\n')
        filewriteParts(file,stringPart2)
        print('mcfd.inp file written in '+dirname)
        i=i+1
        file.close()
    print(i,' files created in corresponding dir')

def fileread(dire,dirname):
    file=open(dire+'\\'+dirname+'\\mcfd.inp','r')
    text=file.readlines()
    for i in text:
        if i[0:7]=='seq.# 2':
            index=text.index(i)
    stringPart1=(text[:index+1])
    stringPart2=(text[index+2:])
    return stringPart1,stringPart2

def filewriteParts(file,part):
    for i in part:
        file.write(i)

def reference_input():
    file_location=input('please enter the location of your states.txt file:')
    dire_location=input('please enter the location of your calculation files:')
    file_location+='\\states.txt'
    return file_location,dire_location

def states_readin(file_location):
    txtfile=open(file_location,'r')
    text=txtfile.readlines()
    text=text[1:]
    for i in range(len(text)):
        text[i]=text[i].split()
    return text

main()

# 这两个文件配合食用
# 可以自动读入文件夹名称以及压强温度速度等
# 并且不需要把整个mcfd文件都写在程序里
# 它会自动根据读取到的第一个inp文件进行配置，也就是说，生成的若干个inp文件中，只有来流性质那一栏有区别
# 但现在有个问题，openpyxl在内部机有吗？
# 下一步打算进行txt文件读取相关信息