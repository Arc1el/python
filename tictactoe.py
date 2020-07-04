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
            ver0 = []; ver1 = []; ver2 = []; ver3 = []; ver4 = []; ver5 = []; ver6 = [];
            hor0 = []; hor1 = []; hor2 = []; hor3 = []; hor4 = []; hor5 = []; hor6 = [];
            dia0 = []; dia1 = [];
            printBoard()
        else:
            print("대전횟수 :", winCount+loseCount+drawCount, "이긴횟수 :", winCount)
            break
    elif result == "lose":
        loseCount += 1
        print("유저 패배!")
        break
    elif result == "draw":
        drawCount += 1
        print("비김!")

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

    while True:
        a = random.randrange(0, 7)
        b = random.randrange(0, 7)
        if board[a][b] == ' ':
            board[a][b] = com
            break

    ver0 = []; ver1 = []; ver2 = []; ver3 = []; ver4 = []; ver5 = []; ver6 = [];
    for i in range(7):
        ver0.append(board[i][0])
    for i in range(7):
        ver1.append(board[i][1])
    for i in range(7):
        ver2.append(board[i][2])
    for i in range(7):
        ver3.append(board[i][3])
    for i in range(7):
        ver4.append(board[i][4])
    for i in range(7):
        ver5.append(board[i][5])
    for i in range(7):
        ver6.append(board[i][6])

    hor0 = []; hor1 = []; hor2 = []; hor3 = []; hor4 = []; hor5 = []; hor6 = [];
    for i in range(7):
        hor0.append(board[0][i])
    for i in range(7):
        hor1.append(board[1][i])
    for i in range(7):
        hor2.append(board[2][i])
    for i in range(7):
        hor3.append(board[3][i])
    for i in range(7):
        hor4.append(board[4][i])
    for i in range(7):
        hor5.append(board[5][i])
    for i in range(7):
        hor6.append(board[6][i])

    dia0 = []; dia1 = [];
    for i in range(7):
        dia0.append(board[i][i])
    col = 6
    for i in range(7):
        dia1.append(board[col][i])
        col = col - 1

    win = [me, me, me, me, me, me, me]
    lose = [com, com, com, com, com, com, com]

    if ((ver0 == win) or (ver1 == win) or (ver2 == win) or (ver3 == win) or (ver4 == win) or (ver5 == win) or
            (ver6 == win) or (hor0 == win) or (hor1 == win) or (hor2 == win) or (hor3 == win) or (hor4 == win)
            or (hor5 == win) or (hor6 == win) or (dia0 == win) or (dia1 == win)):
        result = "win"
    elif ((ver0 == lose) or (ver1 == lose) or (ver2 == lose) or (ver3 == lose) or (ver4 == lose) or (ver5 == lose) or
          (ver6 == lose) or (hor0 == lose) or (hor1 == lose) or (hor2 == lose) or (hor3 == lose) or (hor4 == lose) or
          (hor5 == lose) or (hor6 == lose) or (dia0 == lose) or (dia1 == lose)):
        result = "lose"

