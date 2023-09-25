print('***杨辉三角形生成器***')
def triangle(x):
        M=[1,]
        while x>len(M):
                print(M)
                N=tuple(M)
                n=1
                while n<len(M):
                        M[n]=N[n-1]+N[n]
                        n=n+1
                M.append(1)
while 1:
        x=input('请输入所需要的阶数：')
        triangle(int(x)+1)