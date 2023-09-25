print('***杨辉三角形生成器***')
def triangle(x,y):
        M=[1,]
        if y==0:
                x=x-1
        while x>len(M):
                if y==1:
                        print(M)
                N=tuple(M)
                n=1
                while n<len(M):
                        M[n]=N[n-1]+N[n]
                        n=n+1
                M.append(1)
        if y==0:
                print(M)
                
y=input('是否整体输出？是1 否0 ')
while 1:
        x=input('请输入所需要的阶数：')
        triangle(int(x)+1,int(y))