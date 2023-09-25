from functools import reduce

def f(x,y):
        return int(x)*10+int(y)
def str2num1(s):
        return reduce(f,s)
def str2num2(s):
        return reduce(f,s)/10**len(s)
def str2num(s):
    n=0
    for i in s:
        n=n+1
        if i!='.':
            continue
        return str2num1(s[:n-1])+str2num2(s[n:])

s='0000.006'
z=str2num(s)
print(z)