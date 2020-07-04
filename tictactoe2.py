import random

me = input("Tic-Tac-Toe게임입니다. 원하는 기호를 O X 중에서 선택하세요 : ")
if me == "X":
    com = "O"
else:
    com = 'X'

board = [[' ' for x in range(7)] for y in range(7)]
result = ""
answer = ""
winCount = 0
loseCount = 0
drawCount = 0
boardCount = 0

def printBoard():
    for r in range(7):
        print("  ", end='')
        for i in range(7):
            if i != 6 :
                print(board[r][i] + "|  ", end='')
            else:
                print(board[r][i], end='')

        if r != 6:
            print("\n---|---|---|---|---|---|---")
    print("")

while True:
    printBoard()
    if result == "win":
        winCount += 1
        print("유저 승리!")
        answer = input("다시플레이 하시겠습니까? (y/n) : ")
        if answer == "y":
            board = [[' ' for x in range(7)] for y in range(7)]
            result = ""
            boardCount = 0
            printBoard()
        else:
            print("대전횟수 :", winCount+loseCount+drawCount, "이긴횟수 :", winCount, "진 횟수 :", loseCount, "비긴횟수 :", drawCount)
            break
    elif result == "lose":
        loseCount += 1
        print("유저 패배!")
        answer = input("다시플레이 하시겠습니까? (y/n) : ")
        if answer == "y":
            board = [[' ' for x in range(7)] for y in range(7)]
            result = ""
            boardCount = 0
            printBoard()
        else:
            print("대전횟수 :", winCount + loseCount + drawCount, "이긴횟수 :", winCount, "진 횟수 :", loseCount, "비긴횟수 :", drawCount)
            break
    elif result == "draw":
        drawCount += 1
        print("비김!")
        answer = input("다시플레이 하시겠습니까? (y/n) : ")
        if answer == "y":
            board = [[' ' for x in range(7)] for y in range(7)]
            result = ""
            boardCount = 0
            printBoard()
        else:
            print("대전횟수 :", winCount + loseCount + drawCount, "이긴횟수 :", winCount, "진 횟수 :", loseCount, "비긴횟수 :", drawCount)
            break

    while True:
        x = int(input("(0-6)사이의 x좌표를 입력하세요 : "))
        if (x >= 0) & (x <= 6):
            break
        else:
            print("잘못된 범위의 x를 입력하였습니다. 다시 입력하세요")

    while True:
        y = int(input("(0-6)사이의 y좌표를 입력하세요 : "))
        if (y >= 0) & (y <= 6):
            break
        else:
            print("잘못된 범위의 y를 입력하였습니다. 다시 입력하세요")

    if board[x][y] != ' ':
        print("잘못된 위치입니다.")
        continue
    else:
        board[x][y] = me
        boardCount += 1

    while True:
        a = random.randrange(0, 7)
        b = random.randrange(0, 7)
        if board[a][b] == ' ':
            board[a][b] = com
            boardCount += 1
            break

    # 대각검사
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[2][2] == board[3][3]) \
            and (board[3][3] == board[4][4]) and (board[4][4] == board[5][5]) and (board[5][5] == board[6][6]):
        if board[6][6] == me:
            result = "win"
        elif board[6][6] == com:
            result = "lose"

    if (board[0][6] == board[1][5]) and (board[1][5] == board[2][4]) and (board[2][4] == board[3][3]) \
            and (board[3][3] == board[4][2]) and (board[4][2] == board[5][1]) and (board[5][1] == board[6][0]):
        if board[6][0] == me:
            result = "win"
        elif board[6][0] == com:
            result = "lose"

    # 가로검사
    for i in range(7):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) and (board[i][2] == board[i][3])\
                and (board[i][3] == board[i][4]) and (board[i][4] == board[i][5]) and (board[i][5] == board[i][6]):
            if board[i][6] == me:
                result = "win"
            elif board[i][6] == com:
                result = "lose"

    # 세로검사
    for i in range(7):
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[2][i] == board[3][i])\
                and (board[3][i] == board[4][i]) and (board[4][i] == board[5][i]) and (board[5][i] == board[6][i]):
            if board[6][i] == me:
                result = "win"
            elif board[6][i] == com:
                result = "lose"

    # 비기는경우
    if boardCount >= 49:
        result = "draw"
