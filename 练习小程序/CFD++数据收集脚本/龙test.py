import pandas as pd

# 读取Excel文件
df = pd.read_excel('data1.xlsx', header=None)

# 将数据从一列转换为多列
new_df = df.values.reshape(-1, 1000).T

new_df=pd.DataFrame(new_df)

new_df.to_excel('new_data666777.xlsx', header=None, index=None)
# 将数据保存到Excel文件
#new_df.to_excel('new_data.xlsx', header=None, index=None)