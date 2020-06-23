PI = 3.14159265358979

def main() :
    radius = float(input("원의 반지름을 입력하시오 : "))
    print("원의면적 : ", getArea(radius))
    print("원의둘레 : ", getCircum(radius))

def getArea(radius) :
    return PI * radius* radius

def getCircum(radius) :
    return 2 * PI * radius

main()
