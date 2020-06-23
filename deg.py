def selectMenu() :
    print("'c' 섭씨온도에서 화씨온도로 변환")
    print("'f' 화씨온도에서 섭씨온도로 변환")
    print("'q' 종료")
    print("==============================")

def c2f(c_temp) :
    return 9.0 / 5.0 * c_temp +32

def f2c(f_temp) :
    return (f_temp - 32.0) * 5.0 / 9.0

selectMenu()
choice = input("메뉴를 선택하세요")
if choice == "c" :
    temp = float(input("섭씨온도 : "))
    print("화씨온도 : ", c2f(temp))
elif choice == "f" :
    temp = float(input("화씨온도 : "))
    print("섭씨온도 : ", f2c(temp))
elif choice == "q" :
    print("종료합니다.")
else :
    print("c, f, q 중 하나를 입력하세요")
