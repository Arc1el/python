for a in range(1, 101) :
    for b in range(a, 101) :
        for c in range(b, 101) :
            if a*a+b*b == c*c :
                print(a, b, c)
