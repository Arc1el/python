def alphaToLow(word) :
    result = ""
    for char in word :
        if(char.isalpha()) :
            result += char
    return result.lower()

words = set()
fileName = input("입력할 파일의 경로 및 파일명 : ")
file = open(fileName, "r")

for line in file :
    lineWords = line.split()

    for word in lineWords :
        words.add(alphaToLow(word))

print("\n사용된 단어의 갯수 : ", len(words))
print("사용된 단어가 저장된 집합 출력 : ", words)
