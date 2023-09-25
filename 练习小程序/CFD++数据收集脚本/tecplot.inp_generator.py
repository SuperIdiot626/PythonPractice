import os
def traversedir(ini_dir):                                   #traverse all dirs, secondary dirs included
    i=0
    os.chdir(ini_dir)                                       #first change into target dir                                   #check if there is target file in the initial dir
    secondarydirlsit=os.listdir(ini_dir)                    #list the secondary dics of the initial dir
    secondarydirlsit.sort()                                 #sort the dir list
    for dir in secondarydirlsit:
        wholedir=os.path.join(ini_dir,dir)
        if os.path.isdir(wholedir):
            os.chdir(wholedir)
            file=open('tecout.inp','w')   
            file.write('1\n1\n')
            file.close()
            i+=1
            print('tecout.inp written in '+wholedir)
        else:
            continue
    print('All done! '+str(i)+' files written in total')
target_dir=input('please enter your dir: ')
traversedir(target_dir)