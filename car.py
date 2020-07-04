class Car :
    def __init__(self, speed=0, gear=1, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def __str__(self):
        return '(%d, %d, %s)' % (self.__speed, self.__gear, self.__color)

myCar1 = Car()
print("myCar1 : ", myCar1)
print("my car speed : ", myCar1._Car__speed)
print("my car gear : ", myCar1._Car__gear)
print("my car color : ", myCar1._Car__color)

myCar2 = Car()
print("myCar2 : ", myCar2)
myCar2.setGear(3)
myCar2.setSpeed(100)
print("myCar2 : ", myCar2)
print("my car speed : ", myCar2._Car__speed)
print("my car gear : ", myCar2._Car__gear)
print("my car color : ", myCar2._Car__color)
