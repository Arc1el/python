for tempF in range(0, 100+1, 10) :
    tempC = (tempF - 32.0) * 5.0 / 9.0
    print(tempF, "->", round(tempC, 2))
