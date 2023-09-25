import random,time
nums=1000000
a=1
b=2
timeStart=time.time()
for i in range(nums):
    c=max(a,b)
print(time.time()-timeStart)

timeStart=time.time()
for i in range(nums):
    if a>=b:
        c=a
print(time.time()-timeStart)