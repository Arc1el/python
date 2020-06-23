from random import randint
def game(player) :
    while True:
        player = input("rock, scissors, paper 중에서 하나를 입력하고, 게임을 끝내려면 q를 입력하세요 :")
        if player == "q" :
            return
        elif player == "scissors":
            playerNum = 0
        elif player == "rock" :
            playerNum = 1
        elif player == "paper" :
            playerNum = 2
        else :
            continue

        list = ["scissors", "rock", "paper"]
        comNum = randint(0,2)
        print("user :", player, "computer :", list[comNum])

        if playerNum-comNum == 0 :
            print("무승부")
        elif playerNum-comNum == -2 or playerNum-comNum==1 :
            print("유저승리!!")
        else :
            print("컴퓨터 승리!!")

player = input("게임을 시작하려면 s를 입력하세요 :")
if player == "s" :
    print("게임이 시작되었습니다.")
    game(player)
