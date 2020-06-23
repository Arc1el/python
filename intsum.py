sum = 0

intMax = int(input("어디까지 계산할까요 : "))
for i in range(1, intMax+1) :
    sum = sum + i

print("1부터", intMax, "까지의 정수의 합 =", sum)
