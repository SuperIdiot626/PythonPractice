print('******九九乘法表生成器*****')
i,j=1,1
while i<10:
    j=1
    while j<=i:
        print('%d×%d=%d'%(j,i,i*j),end=" ")
        j+=1
    i+=1
    print('\n')