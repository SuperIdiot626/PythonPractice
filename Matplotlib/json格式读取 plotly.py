# -*- coding: utf-8 -*-
import json
import plotly.express   as px                       #缩写为plt，国际惯例
import pandas           as pd
from plotly.graph_objs import Bar,Layout
from plotly import offline

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

data=pd.DataFrame(
    data=zip(longs,latis,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()

fig=px.scatter(
    #x=longs,
    #y=latis,
    #labels={'x':'经度','y':'纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title='gloal_earthquake',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('gloal_earthquake.html')
fig.show()

'''
readable_file='readable_eq_data.json'
with open(readable_file,'w') as f:
    json.dump(all_eq_data,f,indent=4)
'''