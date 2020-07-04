sum = 0
num = 1

while num <= 100 :
    if num %3 == 0 :
        sum += num
    num += 1

print("1부터 100사이의 모든 배수의 합은 %d 입니다." %sum)
