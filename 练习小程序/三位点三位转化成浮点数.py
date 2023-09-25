from functools import reduce

def f(x,y):
        return int(x)*10+int(y)
def str2num1(s):
        return reduce(f,s)
def str2num2(s):
        return reduce(f,s)/10**len(s)
def str2num(s):
        return str2num1(s[:3])+str2num2(s[4:7])

s='123.456'
z=str2num(s)
print(z)