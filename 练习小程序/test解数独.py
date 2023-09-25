from calendar import c


board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board: list[list[str]]) -> bool:
        arrays=[]       #列
        grids=[]        #格子
        for i in range(9):
            arrays.append([])
            for j in board:
                arrays[i].append(j[i])
        for i in range(3):
            for j in range(3):
                grids.append([])
                for m in range(3):
                    for n in range(3):
                        grids[i*3+j].append(arrays[3*j+n][3*i+m])

        a=5
        b=9
        c=100

        a=a-1
        b=b-1
        board[a][b]=c
        arrays[b][a]=c
        grids[int(a/3)*3+int(b/3)][a%3*3+b%3]=c


        # print('********************************************')
        # for i in board:
        #     print(i)
        # print('********')
        # for i in arrays:
        #     print(i)
        # print('***********')
        # for i in grids:
        #     print(i)
        
        numbers=['1','2','3','4','5','6','7','8','9']
        possibleAnswer=[]
        possibleAnswerNum=[]
        for i in range(9):
            possibleAnswerNum.append([])        #先确定是否能填入数字
            possibleAnswer.append([])           #再确定能填入哪些数字
            for j in range(9):
                possibleAnswer[i].append([])    #再确定能填入哪些数字
                possibleAnswerNum[i].append(0)
                if board[i][j]!='.':
                    continue
                else:
                    possibleAnswer[i][j]=numbers[:]
                    for index in board[i]:                                  #针对每行去重
                        if index!='.':
                            possibleAnswer[i][j].remove(index)
                    for index in arrays[j]:
                        if index!='.' and (index in possibleAnswer[i][j]):  #针对每列去重
                            possibleAnswer[i][j].remove(index)
                    for index in grids[int(i/3)*3+int(j/3)]:
                        if index!='.' and (index in possibleAnswer[i][j]):  #针对每个大格去重
                            possibleAnswer[i][j].remove(index)
                    possibleAnswerNum[i][j]=len(possibleAnswer[i][j])

        for i in range(9):
            for j in range(9):
                if possibleAnswer[i][j]==0:
                    continue
                else:
                    
                    pass

        print('***********')
        for i in possibleAnswer:
            print(i)
        for i in possibleAnswerNum:
            print(i)
        print('*************************')
        return False

print(isValidSudoku(board))