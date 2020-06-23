pytha = []
for a in range(1,31):
    for b in range(a, 31):
        for c in range(b, 31):
            if(a**2 + b**2 == c**2) :
                pytha.append ((a, b, c))

pytha2 = [(x,y,z) for x in range(1, 31) for y in range(x, 31)
          for z in range(y, 31) if x**2 + y**2 == z**2]

print(pytha, "\n")
print(pytha2)
