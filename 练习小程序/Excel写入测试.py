#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Author Wyz

import openpyxl
import openpyxl.utils

wb=openpyxl.Workbook()                      #创建新的excel文件

#sheet=wb.get_active_sheet()                #获取当前处于活动的sheet，该方法已失效
sheet=wb.active                             #获取当前处于活动的sheet，书中的方法过时了
sheet.title='Data Output'


i,j,k=0,0,0
number=[]
while i<5:
    number.append([])
    j=0
    while j<10:
        k+=1
        j+=1
        number[i].append(k)
    i+=1


data=number
row_num=len(data)

i=0
while i<row_num:
    j=0
    column_number=len(data[i])
    while j<column_number:
        sheet.cell(i+1,j+1).value=data[i][j]
        print(data[i][j])
        j+=1
    i+=1





wb.save('wtf.xlsx')                         #将创建的excel文档以此名称保存

