facto=1.0

inputNum = int(input("정수를 입력하시오 : "))
for i in range(1, inputNum+1) :
    facto = facto * i
    print (i, end=" ")

print("\n",inputNum, "!은", facto, "이다.")
