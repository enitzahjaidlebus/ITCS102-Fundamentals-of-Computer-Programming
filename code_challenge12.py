for i in range(1, 7, 1):
    for j in range(7, i, -1):
        print(" ", end=" ")
    for b in range(i, 0, -1):
        print(b, end=" ")
    for s in range(2, i+1, 1):
        print(s, end=" ")
    print(" ")