import turtle

poly = turtle.Turtle()

sideNum= 3
sideLen = 200
polyAngle = 360.0 / sideNum

for i in range(sideNum) :
    poly.forward(sideLen)
    poly.right(polyAngle)
