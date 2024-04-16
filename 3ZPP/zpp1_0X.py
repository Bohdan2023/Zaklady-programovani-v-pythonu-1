x = int(input("number:"))
for z in range(1, x + 1):
    if x >= z:
        y = z
        for i in range(y):
            for j in range(y):
                if (i < y - 1 and j < y - 1 and i > 0 and j > 0):
                    print(" ", end = " ")
                else:
                    print("*", end = " ")
            print(" ")