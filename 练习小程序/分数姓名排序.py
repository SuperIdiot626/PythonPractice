# -*- coding: utf-8 -*-
print('***分数姓名排序***')

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
        return t[-1]
def by_name(t):
        return t[0]
f=by_score
while 1:
        x=int(input('排列规则？ 姓名1 分数0： '))
        n=int(input('排列顺序？ 顺序1 逆序0： '))
        if x!=0:
                f=by_name
                n=1-n
        print(sorted(L, key=f,reverse=n))