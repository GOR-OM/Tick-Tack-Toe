def sum(a,b,c):
    return a+b+c 

def printBoard(xState, yState):
    results = {}
    for i in range(9):
        results[i] = 'X' if xState[i] else ('O' if yState[i] else i)

    print(f"{results[0]} | {results[1]} | {results[2]}")
    print(f"--|---|--")
    print(f"{results[3]} | {results[4]} | {results[5]}")
    print(f"--|---|--")
    print(f"{results[6]} | {results[7]} | {results[8]}")

def isWin(xState,yState):
    wins = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("X won the match")
            return 1
        elif(sum(yState[win[0]],yState[win[1]],yState[win[2]])==3):
            print("O won the match")
            return 0
    else :
        return -1 

def isDraw(xState, yState):
    return all(xState[i] or yState[i] for i in range(9))

if __name__ ==  "__main__" : 
    xState = [0, 0, 0, 0, 0, 0, 0, 0,0]
    yState = [0, 0, 0, 0, 0, 0, 0, 0,0]
    turn = 1 # 1 for X and  0 for O 
    print("Welcome to Tic Tack Toe")
    while (True):
        printBoard(xState,yState)
        if turn == 1:
            print("X chance")
            value = int(input("Please enter a value (0-8): "))
            if 0 <= value <= 8 and xState[value] == 0 and yState[value] == 0:
                xState[value] = 1
                # isWin(xState,yState)
                turn = 0
            else:
                print("Invalid input. Try again.")
        else:
            print("O chance")
            value = int(input("Please enter a value (0-8): "))
            if 0 <= value <= 8 and xState[value] == 0 and yState[value] == 0:
                yState[value] = 1
                # isWin(xState,yState)
                turn = 1
            else:
                print("Invalid input. Try again.")
        check = isWin(xState,yState)
        if check != -1 : 
            break
        elif isDraw(xState, yState):
            print("It's a draw!")
            break
    print("---------------------------------------------")
    printBoard(xState,yState)
