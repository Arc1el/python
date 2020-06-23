dog = []
while True :
    name = input("애완견의 이름을 입력하세요(종료시 엔터키)")
    if name == "" :
        break
    dog.append(name)

print("애완견들의 이름 : ")
for name in dog :
    print(name, end=" ")
