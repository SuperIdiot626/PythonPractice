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
        
        for i in range(9):
            for j in range(9):
                index=board[i][j]
                if index!='.':
                    # print(index)
                    temp_board=  board[i][:]
                    temp_arrays=arrays[j][:]
                    temp_grids=  grids[int(i/3)*3+int(j/3)][:]
                    temp_board.remove(index)
                    temp_arrays.remove(index)
                    temp_grids.remove(index)
                    # print(temp_board)
                    # print(temp_arrays)
                    # print(temp_grids)
                    # if  (index not in temp_board) and (index not in temp_arrays) and (index not in temp_grids):
                    #             continue
                    # else:
                    #     return False
                    if  (index in temp_board) or (index  in temp_arrays) or (index in temp_grids):
                        return False
                    else:
                        continue
        return True
print(isValidSudoku(board))