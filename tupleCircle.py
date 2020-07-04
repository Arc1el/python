import math
def calCircle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float(input("원의 반지름을 입력하세요 : "))
(a, c) = calCircle(radius)
print("원의 넓이는 ", a, "이고, 원의 둘레는 ", c, "이다.")
