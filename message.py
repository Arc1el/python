table = {"B4" : "Before",
         "TX" : "Thanks",
         "BBL" : "Be Back Later",
         "BCNU" : "Be Seeing You",
         "HAND" : "Have A Nice Day"}

message = input("문장을 입력하세요 : ")
words = message.split()
print("message.split() 후 출력 : ", words)
result = " "
for word in words :
    if word in table :
        result += table[word] + " "
    else :
        result += word + " "

print(result)
