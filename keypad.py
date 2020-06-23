string = 'ABC:DEF:GHI:JKL:MNO:PQRS:TUV:WXYZ'
splitStr = string.split(":")

while True:
    splitIndex = int(input('2~9 사이의 정수를 입력하세요 (종료 : 0) : '))
    if (splitIndex==0) :
        print("프로그램을 종료합니다")
        break;

    print(splitStr[splitIndex-2])
