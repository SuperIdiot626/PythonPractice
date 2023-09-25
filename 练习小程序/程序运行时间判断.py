# -*- coding: utf-8 -*-
import time
from functools import wraps

def metric(func):  
        def wrapper(*args):
                x=time.time()
                func(*args)
                y=time.time()      
                print('%s executed in %s ms' % (func.__name__, y-x))
                return func(*args)
        return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.0012)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')