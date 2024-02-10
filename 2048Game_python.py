import random

import copy

boardsize= 4

def display():
    print()
    #Finding the largest number in the data
    largest=board[0][0]
    for row in board:
        for element in row:
            if element>largest:
                largest=element
    

    #Find the number of spaces
    spacenum= len(str(largest))


    for row in board:
        Row1="|"
        for element in row:
            if element==0:
                Row1+=" "*spacenum+"|"
            else:
                Row1+=(" "*(spacenum-len(str(element))))+str(element)+'|'
        print(Row1)
    print()





#This function merges one row left:

def mergeOneRowL(row):
    # Move everything as far to the left as possible
    for j in range(boardsize - 1):
        for i in range(boardsize -1,-1):
            if row[i-1] ==0:
                row[i-1]=row[i]
                row[i]=0
    

    for i in range (boardsize -1):
        if row[i]==row[i+1]:
            row[i] *=2
            row[i+1]=0

    for i in range (boardsize-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0
    return row


def merge_left(currentBoard):
    for i in range(boardsize):
        currentBoard[i]=mergeOneRowL(currentBoard[i])
    return currentBoard

def reverse(row):

    new=[]
    for i in range(boardsize-1,-1,-1):
        new.append(row[i])
    return new

def merge_right(currentBoard):

    for i in range(boardsize):

        currentBoard[i]=reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i]= reverse(currentBoard[i])
    return currentBoard

def transpose(currentBoard):
    for j in range(boardsize):
        for i in range(j,boardsize):
            if not i==j:
                temp=currentBoard[j][i]
                currentBoard[j][i]=currentBoard[i][j]
                currentBoard[i][j]=temp
    return currentBoard


def merge_up(currentBoard):

    currentBoard=transpose(currentBoard)
    currentBoard=merge_left(currentBoard)
    currentBoard=transpose(currentBoard)
    
    return currentBoard


def merge_down(currentBoard):

    currentBoard=transpose(currentBoard)
    currentBoard=merge_right(currentBoard)
    currentBoard=transpose(currentBoard)

    return currentBoard

def pickNewValue():
    if random.randint(1,8)==1:
        return 4
    else:
        return 2

# This add a value to the board

def addNewValue():
    while True:
        rowNum = random.randint(0, boardsize - 1)
        colNum = random.randint(0, boardsize - 1)

        if board[rowNum][colNum] == 0:
            board[rowNum][colNum] = pickNewValue()
            break

def won():
    for row in board:
        if 2048 in row:
            return True
    return False

def noMoves():
    tempBoard1 = copy.deepcopy(board)
    tempBoard2 = copy.deepcopy(board)

    tempBoard1 = merge_down(tempBoard1)
    if tempBoard1 == tempBoard2:
        tempBoard1 = merge_up(tempBoard1)
        if tempBoard1 == tempBoard2:
            tempBoard1 = merge_left(tempBoard1)
            if tempBoard1 == tempBoard2:
                tempBoard1 = merge_right(tempBoard1)
                if tempBoard1 == tempBoard2:
                    return True
    return False
        
            




board = []
for i in range(boardsize):
    row = []
    for j in range(boardsize):
        row.append(0)
    board.append(row)

numneeded = 2
while numneeded > 0:
    rowNum = random.randint(0, boardsize - 1)
    colNum = random.randint(0, boardsize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numneeded -= 1

print("""Welcome to game 2048! \n 'a' to merge left \n 'd' to merge right\n 's' to merge down \n 'w' to merge up""")

print('Here is the starting board')
display()

gameOver = False

while not gameOver:
    move = input('Please enter the value you want to merge: ')

    tempBoard = copy.deepcopy(board)

    validinput = True

    if move.lower() == "d":
        board = merge_right(board)
    elif move.lower() == "a":
        board = merge_left(board)
    elif move.lower() == "w":
        board = merge_up(board)
    elif move.lower() == "s":
        board = merge_down(board)
    else:
        validinput = False

    if not validinput:
        print("Your input is not valid, please try again")
    else:
        if board == tempBoard:
            print('Try in a different direction')
        else:
            if won():
                display()
                print("You won!!")
                gameOver = True
            else:
                addNewValue()
                display()

            if noMoves():
                print("Game over")
                gameOver = True

    

















