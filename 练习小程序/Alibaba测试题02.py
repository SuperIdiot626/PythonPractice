#!/usr/bin/env python3
# -*- coding: utf-8 -*-

namelist={}
namenum=0

def name_test():
    global namelist
    global namenum
    nameInput=input()
    if namelist.get(nameInput):
        print('acount existed')
        return 0
    elif len(nameInput)<6 or  len(nameInput)>12:
        print('illegal length')
        return 0
    elif not nameInput.isalpha():
        print('illegal charactor')
        return 0
    print('registration complete')
    namenum+=1
    namelist[nameInput]=namenum

num_try=int(input())
for _ in range(num_try):
    name_test()

# registration complete
# illegal length
# acount existed
# illegal charactor