import time
import math
# t = 60
# print("**************带时间的进度条**************")
# start = time.perf_counter()
# for percent in range(t + 1):
#     finsh = "|" * percent
#     need_do = "-" * (t - percent)
#     progress = (percent / t) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
#     time.sleep(0.05)

# percent=0
# totalnum=300
# start = time.perf_counter()
# for lll in range(totalnum):
#     finsh = "|" * int(percent/totalnum*50)
#     need_do = "-" * int((1-percent/totalnum)*50)
#     progress = (percent / totalnum) * 100
#     dur = time.perf_counter() - start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="")
#     percent+=1
#     time.sleep(0.01)

def permute(nums:int,timeit:int) -> list[list[int]]:
    nums=list(range(nums))
    res, path, used = [], [], [False] * len(nums)

    if timeit==1:
        percent=[0,0]
        totalnum=math.factorial(len(nums))
        start = time.perf_counter()

    def dfs() -> None:
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]: continue
            path.append(nums[i])
            
            if timeit==1:
                percent[0]+=1
                if percent[0]==int(totalnum/100):
                    percent[1]+=1
                    percent_Decimal=percent[1]/100/2.718281828459
                    finsh = "|" * int(percent_Decimal*50)
                    need_do = "-" * int((1-percent_Decimal)*50)
                    dur = time.perf_counter() - start
                    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(percent_Decimal*100, finsh, need_do, dur), end="")
                    percent[0]=0

            used[i] = True
            dfs()
            # 回溯的过程中，将当前的节点从 path 中删除
            path.pop()
            used[i] = False
    dfs()
    return res

(permute(9,1))
