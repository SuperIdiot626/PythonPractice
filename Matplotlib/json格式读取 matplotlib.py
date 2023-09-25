# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt                     #缩写为plt，国际惯例
filename='eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data=json.load(f)

all_eq_dicts=all_eq_data['features']
mags,titles,longs,latis=[],[],[],[]
for i in all_eq_dicts:
    mag=i["properties"]["mag"]
    title=i["properties"]["title"]
    long=i["geometry"]["coordinates"][0]
    lati=i["geometry"]["coordinates"][1]
    mags.append(mag)
    titles.append(title)
    longs.append(long)
    latis.append(lati)

print(len(mags))
fig,ax=plt.subplots()
ax.scatter(longs,latis,s=5,c=mags,cmap=plt.cm.jet)  
ax.axis([-190,190,-90,90])                          #设置两个坐标轴的取值范围     


ax.set_title("earthquake spread",fontsize=24)       #设置图表总标题
ax.set_xlabel("longitude",fontsize=14)              #设置坐标轴标题
ax.set_ylabel("latitude",fontsize=14)


plt.show() 
'''
readable_file='readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data,f,indent=4)
'''