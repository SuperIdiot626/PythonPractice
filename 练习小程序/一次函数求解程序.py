print('***一元一次方程求解***')
def solve(a,b):
    x=-b/a
    print('%.5f'%x)
while 1:
    y=input('请输入一次项系数：')
    z=input('请输入常数项系数：')
    y=int(y)
    z=int(z)
    solve(y,z)