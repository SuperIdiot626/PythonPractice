def fib(m):
    a,b,n=1,0,1
    print(a)
    while n<m:
        a,b=a+b,a
        print(a)
        n=n+1
    return(a)
    
print('***斐波那契数列生成器***')
while 1:
    m=input('请输入所需要的数列总序数:')
    m=int(m)
    print('第%d个斐波那契数是%d\n'%(m,fib(m)))