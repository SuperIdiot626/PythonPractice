pi=''
with open('pi.txt') as file1:
    for i in file1:
        pi+=i.strip()

if '120372' in pi:
    print("yes!")
else:
    print('no')