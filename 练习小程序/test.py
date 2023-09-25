board= [[".",".",".","2",".",".",".","6","3"],
        ["3",".",".",".",".","5","4",".","1"],
        [".",".","1",".",".","3","9","8","."],
        [".",".",".",".",".",".",".","9","."],
        [".",".",".","5","3","8",".",".","."],
        [".","3",".",".",".",".",".",".","."],
        [".","2","6","3",".",".","5",".","."],
        ["5",".","3","7",".",".",".",".","8"],
        ["4","7",".",".",".","1",".",".","."]]

def SudokuMessage(board: list[list[str]]) -> list[list[str]]:
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
        return arrays,grids

def isValidSudoku123(board,arrays,grids) -> bool:
        for i in range(9):
            for j in range(9):
                index=board[i][j]
                if index!='.':
                    temp_board=  board[i][:]
                    temp_arrays=arrays[j][:]
                    temp_grids=  grids[int(i/3)*3+int(j/3)][:]
                    temp_board.remove(index)
                    temp_arrays.remove(index)
                    temp_grids.remove(index)
                    if  (index in temp_board) or (index  in temp_arrays) or (index in temp_grids):
                        return False
                    else:
                        continue
        return True

def possibleSolve(board:list[list[str]],arrays:list[list[str]],grids:list[list[str]])->list[list[str]]:
        possibleAnswer=[]
        possibleAnswerNum=[]
        restart=0
        numbers=['1','2','3','4','5','6','7','8','9']
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
                    if possibleAnswerNum[i][j]==1:                                #如果等于1，说明该位置数字确定
                        board[i][j]=possibleAnswer[i][j][0]
                        arrays[j][i]=possibleAnswer[i][j][0]
                        grids[i//3*3+j//3][i%3*3+j%3]=possibleAnswer[i][j][0]
                        restart=1
                        possibleAnswer[i][j]=[]
                        possibleAnswerNum[i][j]=0
        if restart==1:
            possibleAnswer,possibleAnswerNum=possibleSolve(board,arrays,grids)
        return possibleAnswer,possibleAnswerNum

def solveTheSodu(board):
        #a=board
        sudoArray,sudoGrids=SudokuMessage(board)
        possibleAnswer,possibleAnswerNum=possibleSolve(board,sudoArray,sudoGrids)
        for i in board:
            print(i,'dd')
        # for i in possibleAnswerNum:
        #     print(i)
        tmp_possibleAnswer   =possibleAnswer[:]
        tmp_possibleAnswerNum=possibleAnswerNum[:]
        for i in range(9):
            for j in range(9):
                #print('i,j=',i,j)
                broken=0
                if tmp_possibleAnswerNum[i][j]==0:
                    continue
                else:
                    tmp_board=[board[i][:] for i in range(len(board))]
                    tmp_sudoArray=[sudoArray[i][:] for i in range(len(sudoArray))]
                    tmp_sudoGrids=[sudoGrids[i][:] for i in range(len(sudoGrids))]
                    tmp_possibleAnswer   =[possibleAnswer[i][:] for i in range(len(possibleAnswer))]
                    tmp_possibleAnswerNum=[possibleAnswerNum[i][:] for i in range(len(possibleAnswerNum))]
                    index=0
                    length=len(tmp_possibleAnswer[i][j])
                    for time in range(length):
                        broken=0
                        tmp_board=[board[i][:] for i in range(len(board))]
                        tmp_sudoArray=[sudoArray[i][:] for i in range(len(sudoArray))]
                        tmp_sudoGrids=[sudoGrids[i][:] for i in range(len(sudoGrids))]
                        #print(index,i,j,tmp_possibleAnswer[i][j])
                        pa=tmp_possibleAnswer[i][j][index]
                        tmp_board[i][j]=pa
                        tmp_sudoArray[j][i]=pa
                        tmp_sudoGrids[i//3*3+j//3][i%3*3+j%3]=pa
                        try:
                            tmp_possibleAnswer2,tmp_possibleAnswerNum2=possibleSolve(tmp_board,tmp_sudoArray,tmp_sudoGrids)
                            # for ls in tmp_possibleAnswer2:
                            #     print(ls)
                        except:
                            broken=1

                        for k,x in enumerate(tmp_board):            #此处有问题，即使存在'.'也不代表该值无解（吗？）
                            for l,y in enumerate(x):                #要从行、列、格三个角度处理这个数据
                                if y=='.' and tmp_possibleAnswerNum2[k][l]==0:
                                    broken=1
                                    # print(k,l)
                                    break
                            if broken==1:
                                break
                        for ss in  tmp_board:
                            print(ss,'ss')
                        for ss in  tmp_possibleAnswer2:
                            print(ss)
                        for ss in  tmp_possibleAnswerNum2:
                            print(ss,'aa')
                        if broken==1:
                            print('被移出的是',i+1,j+1,pa)
                            possibleAnswer[i][j].remove(pa)
                            possibleAnswerNum[i][j]-=1
                            # print(possibleAnswerNum[i][j],possibleAnswer[i][j])
                            if possibleAnswerNum[i][j]==1:
                                #print('board 修改',i,j,possibleAnswer[i][j][0])
                                board[i][j]=possibleAnswer[i][j][0]
                                sudoArray[j][i]=possibleAnswer[i][j][0]
                                sudoGrids[i//3*3+j//3][i%3*3+j%3]=possibleAnswer[i][j][0]
                                sudoArray,sudoGrids=SudokuMessage(board)
                                possibleAnswer,possibleAnswerNum=possibleSolve(board,sudoArray,sudoGrids)
                            #print('continue了',index)
                            continue
                        else:
                            print('done')
                            for i in range(9):
                                for j in range(9):
                                    board[i][j]=tmp_board[i][j]
                            return None

solveTheSodu(board)
for i in board:
    print(i)