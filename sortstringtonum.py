inputString = input("문자열을 입력하세요. : ")

alpha = 0
digit = 0
space = 0

for str in inputString :
    if str.isalpha() :
        alpha += 1
    if str.isdigit() :
        digit += 1
    if str.isspace() :
        space += 1

print("알파벳의 갯수 : ", alpha)
print("숫자의 갯수 : ", digit)
print("공백의 갯수 : ", space)
