def lower(L):
    l=[]
    for n in L:
        if isinstance(n,str):
            l.append(n.lower())
    return l

L1 = ['Hello', 'World', 18, 'Apple', None]
lower(L1)
print(lower(L1))
if lower(L1) == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')