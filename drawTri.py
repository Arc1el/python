import turtle as tri

times = 30
tri.shape("turtle")
tri.color("red")
tri.speed("fastest")

for i in range(times) :
    tri.circle(100)
    tri.right(360/times)
