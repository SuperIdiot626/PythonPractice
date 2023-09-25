import time
timenow=time.strftime(("%Y-%m-%d_%H.%M.%S"),time.localtime())
timenow='data_'+timenow+'.xlsx'
print(timenow)