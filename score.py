STUNUM = 5

score = []
sumScore = 0

for i in range(STUNUM) :
    appendScore = int(input("성적을 입력하세요 : "))
    score.append(appendScore)
    sumScore += appendScore

avgScore = sumScore / len(score)

highScore = 0
for i in range(len(score)) :
    if score[i] >= 80 :
        highScore += 1

print("성적평균은", avgScore, "입니다.")
print("80점 이상의 성적을 받은 학생은", highScore, "명입니다.")
