print('***马赫数计算程序***')






k=1.4




while 1:
    
    a=input('请输入波前压强:')#3.14
    b=input('请输入波后压强:')


    
    a=float(a)


    b=float(b)



    c=(k+1)/2/k*((k-1)/(k+1)+b/a)


    c=c**0.5
    #c=pow(c,0.5)



    print('波前压力%.2f，波后压强%.2f,则波前马赫数为%.5f'%(float(a),float(a),float(c)))



    print('则波前马赫数为%f'%c)
    
#为什么一定要运行两次才成功？？
print