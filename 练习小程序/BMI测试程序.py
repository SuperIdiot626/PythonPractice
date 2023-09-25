# -*- coding: utf-8 -*-
w=input('请输入体重：')
h=input('请输入身高：')
w=int(w)
h=int(h)
if h>=5:
    h=h/100
B=w/(h**2)
print('你的BMI指数为：%.2f'%B)
if B<=18.5:
    print('您太轻了！多吃肉！')
elif B<=25:
    print('嗯，身材不错哦！')
elif B<=28:
    print('emmmmm,稍微重，还能接受~')
elif B<=32:
    print('你一定是个资深吃货')
elif B>32:
    print('死胖子，赶紧死开！')