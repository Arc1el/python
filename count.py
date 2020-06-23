fileName = input("파일이름 : ")
file = open(fileName, "r")

dic = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in dic:
            dic[word] = 1
        else :
            dic[word] += 1

print(dic)
