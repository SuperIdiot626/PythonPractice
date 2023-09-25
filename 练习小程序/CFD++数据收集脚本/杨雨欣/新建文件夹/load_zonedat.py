import re
import os
import numpy as np
import pandas as pd

def load_dat(file_url,i):

    file_url = file_url + '\\' + str(i) + '.DAT'
    with open(file_url, 'r') as f:
        all_list = f.readlines()
        print("行数：", len(all_list))
        zone_list = []
        grid_list = []
        grid_point = []
        is_zone = 0
        grid_line_num = 0
        for i, line in enumerate(all_list):
            if is_zone == 0:
                matchZONE = re.search(r'ZONE T', line, re.M|re.I)
                if matchZONE:
                    print('zone', len(zone_list)+1)
                    is_zone = 1
                    continue
            if is_zone == 1:
                is_zone = 2
                grid_line_num = 0
                continue
            if is_zone == 2:
                p_list = line.strip().split()
                num_list = len(p_list)
                if grid_line_num == 0 and num_list == 4:
                    is_zone = 0
                    zone_list.append(grid_list)
                    grid_list = []   
                elif grid_line_num == 4:
                    for p in p_list:
                        grid_point.append(float(p))
                    grid_list.append(grid_point)
                    grid_point = []
                    grid_line_num = 0
                else:
                    # print(p_list)
                    try:
                        for p in p_list:
                            grid_point.append(float(p))
                        grid_line_num += 1
                    except:
                        print(i,line,num_list,"格式不匹配！！！！！！")
                        break
    if len(zone_list):
        zone_numpy = np.array(zone_list[0])
        for i in range(1,len(zone_list)):
            zone_numpy = np.concatenate((zone_numpy,np.array(zone_list[i])), axis=0)
        
    return zone_numpy

# if __name__ == '__main__':
#
#     file_url = input("输入文件路径: ")
#     file_url=file_url+'\\'+'SURFTEC.DAT'
#     if os.path.exists(file_url):
#         zone_numpy = load_dat(file_url)
#         zone_pandas =  pd.DataFrame(zone_numpy)
#         np.save(file_url, zone_numpy)
#         print(zone_pandas)
#     else:
#         print("文件不存在")