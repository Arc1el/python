cols = 6
rows = 6
table = [[0] * cols for i in range(6)]
for row in range(rows):
    for col in range(cols):
        table[row][col] = (row + 1 + col + 1)

for sero in range(6):
    if (sero == 0) :
        print ( "    |", end = " ")
        for garo in range (1,7) :
            print("%3d" %(garo), end = " ")
        print()
        print("-"*30)

    print (sero+1, "  | ", end="")
    for garo in range(6):
        print("%3d" %table[sero][garo], end=" ")
    print()
