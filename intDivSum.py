num = int(input("자리수의 합을 계산하기 위한 값을 입력하시오 : "))

sum = 0
while num > 0 :
    print("현재 취급 숫자는 :", num)
    digit = num % 10
    print("일의자리", digit)
    sum += digit
    print("현재까지 일의자리 누적 :", sum)
    num = num // 10
    print("일의자리를 생략한 나머지 숫자 :",num)

print("자리수의 합은 %d입니다." %sum)
