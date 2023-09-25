import re

phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #定义正则表达式，整数与下划线


def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True


message='asdasd123-456-7891asdzxcq1zxcq2qwxzxc-asd21qwe4zx-c*/q+w1rzxc112-555-8888'
num1='415-555-4242'
num2='321a125a4578'

mo=phoneNumberRegex.search(message)
print(mo.group())
mo=phoneNumberRegex.match(message)
print(mo)

print(isPhoneNumber(num1))
print(isPhoneNumber(num2))



