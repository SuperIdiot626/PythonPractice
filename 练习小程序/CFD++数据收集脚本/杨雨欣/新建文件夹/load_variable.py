import re
def load_vari(file_url, i):
    file_url=file_url+'\\'+str(i)+'.DAT'
    lines=[]
    with open(file_url, 'r') as f:
        for i in f.readlines()[1:24]:
            i=re.sub('[ ",\n]','',i)
            lines.append(i)
    lines[0]='X'
    return lines
