from pprint import pprint


def isValid(ex,row,column,guess):
    row_vals=ex[row]
    if guess in row_vals:
        return False
    valCols=[]
    for i in range(9):
        valCols.append(ex[i][column])
    if guess in valCols:
        return False
    rowStart=(row//3)*3
    colStart=(column//3)*3
    for i in range(rowStart,rowStart+3):
        for j in range(colStart,colStart+3):
            if ex[i][j]==guess:
                return False
    return True



def findNextEmpty(ex):
    for r in range(9):
        for c in range(9):
            if ex[r][c]==-1:
                return r,c
    return None,None


def solve_sudoku(ex):
    row,col=findNextEmpty(ex)
    if row is None:
        return True
    for guess in range(1,10):
        if isValid(ex,row,col,guess):
            ex[row][col]=guess
            if solve_sudoku(ex):
                return True
        ex[row][col]=-1
    return False



if __name__=='__main__':
    example=[
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example))
    pprint(example)