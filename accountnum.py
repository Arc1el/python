account = input("계좌번호 입력 : ")
result = ""

for str in account :
    if str != "-" :
        result += str

print("계좌번호(숫자만) : ", result)
