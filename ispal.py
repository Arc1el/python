def isPal(str) :
    first = 0
    last = len(str) -1

    while True :
        if first > last :
            return True;

        a = str[first]
        b = str[last]

        if a != b :
            return False;

        first += 1
        last -= 1

str = input("문자열을 입력하세요 : ")
str = str.replace(" ", "")

if (isPal(str)==True) :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")
