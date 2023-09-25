print('***回文数查找程序***')
def huiwenshu(n):
        return str(n)==str(n)[::-1]
while 1:
        n=int(input('请输入寻找回文数的范围： '))
        print(list(filter(huiwenshu,range(n))))


