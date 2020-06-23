print("구구단 출력")
print("-"*30)
dan = int(input("몇 단을 출력할까요? "))

i = 1
while i <= 9 :
    print("%d * %d = %d" %(dan, i, dan*i))
    i += 1
    
