import random
counter = 0
num = random.randint(1, 100)
print("1부터 100사이의 숫자를 맞추시오")

while counter < 10 :
    inputNum = int(input("숫자를 입력하십시오 :"))
    counter += 1
    if inputNum < num :
        print("컴퓨터가 생각하는 숫자보다 더 작음!")
    elif inputNum > num :
        print("컴퓨터가 생각하는 숫자보다 더 큼!")
    else :
        break

if inputNum == num :
    print("축하합니다. 정답입니다. 시도횟수=", counter)
else :
    print("정답은", num)
