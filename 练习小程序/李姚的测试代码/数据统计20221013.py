from json.encoder import INFINITY
import os

def datacollect(filename):
    list_t=[]
    list_mvd=[]
    list_aoa=[]
    list_lwc=[]
    file=open(filename)
    text=file.readlines()
    first=True
    for i in text:
        if first:
            first=False
            continue
        i=i.split()
        list_t.append(float(i[3]))
        list_mvd.append(float(i[5]))
        list_aoa.append(float(i[6]))
        list_lwc.append(float(i[9]))
    list_t=list(set(list_t))
    list_mvd=list(set(list_mvd))
    list_aoa=list(set(list_aoa))
    list_lwc=list(set(list_lwc))

    list_t.sort()
    list_mvd.sort()
    list_aoa.sort()
    list_lwc.sort()

    base_lwc=1
    base_aoa=len(list_lwc)*base_lwc
    base_mvd=len(list_aoa)*base_aoa
    base_t=len(list_mvd)*base_mvd


    hashlib=[]
    resultstep=[]
    first=True
    for line in text:
        if first:
            first=False
            continue
        line=line.split()
        a=list_t  .index(float(line[3]))
        b=list_mvd.index(float(line[5]))
        c=list_aoa.index(float(line[6]))
        d=list_lwc.index(float(line[9]))
        hash1=a*base_t+b*base_mvd+c*base_aoa+d*base_lwc
        hash1=(   list_t .index(float(line[3]))*base_t
                +list_mvd.index(float(line[5]))*base_mvd
                +list_aoa.index(float(line[6]))*base_aoa
                +list_lwc.index(float(line[9]))*base_lwc)
        if hash1 not in hashlib:
            hashlib.append(hash1)
            resultstep.append([int(line[1]),])
        else:
            resultstep[hashlib.index(hash1)].append(int(line[1]))
    for index,data in enumerate(resultstep):
        resultstep[index]=min(data)
    
    result=[]
    first=True
    for line in text:
        if first:
            first=False
            continue
        line=line.split()
        if int(line[1]) in resultstep:
            result.append(line)
    
    for i in result:
        print(i[1],i[3],i[5],i[6],i[9],)



def main():
    dir=input('what is your dir')
    filename=input('what is filename')
    os.chdir(dir)
    datacollect(filename)

main()