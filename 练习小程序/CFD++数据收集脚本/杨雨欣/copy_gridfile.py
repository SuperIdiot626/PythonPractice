import os,shutil

target_file='H:\\0610\\0613\\'
src_file='H:\\0610\\Model-Grid\\'
target1=src_file+'cellsin.bin'
target2=src_file+'mcfd.grp'
target3=src_file+'cgrpsin.bin.1'
target4=src_file+'exbcsin.bin'
target5=src_file+'mcfd.bc'
target6=src_file+'nodesin.bin'
i=1
while i<=40:
    dstfile=target_file+str(i)
    os.makedirs(dstfile)
    shutil.copy(target1, dstfile)
    shutil.copy(target2, dstfile)
    shutil.copy(target3, dstfile)
    shutil.copy(target4, dstfile)
    shutil.copy(target5, dstfile)
    shutil.copy(target6, dstfile)
    i=i+1