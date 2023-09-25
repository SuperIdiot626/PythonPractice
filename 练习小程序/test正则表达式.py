def isMatch( s: str, p: str) -> bool:
        i,j=0,0
        lengthS=len(s)
        lengthP=len(p)
        while i<lengthS:
            if j>=lengthP:          #可能出现P遍历完毕范围超界，这种情况直接判定为失败
                print('False_1')
                return False
            elif s[i]==p[j]:
                i+=1
                j+=1
                continue
            elif p[j]=='*':         #遇见星号
                if s[i]==p[j-1]:    #对比上一位
                    j-=1            #如果上一位吻合，就继续
                    continue
                elif p[j-1]!='.':   #上一位不吻合，且不是点
                    j+=1            #说明星号作用范围结束，p位数加一
                    continue        #跳过星号进行下一位对比
                elif p[j-1]=='.':   #上一位不吻合，是点
                    i+=1            #p的位数不变，s位数加一
                    continue        
            elif p[j]=='.':         #遇到点，视为吻合
                i+=1
                j+=1
                continue
            else:
                print('False_2')
                return False
        while j<lengthP:          #P未遍历完毕的情况
            j+=1
            if p[j]=='*' or p[j]=='.':
                continue
            else:
                print(j)
                print('False_3')
                return False
        print(j,lengthP)
        return True

s='plaaaan'
p='.*n'
print(isMatch(s,p))