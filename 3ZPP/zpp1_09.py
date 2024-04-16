def pocatecny_stav(p):
    if p > 7:
        print("a b c d e f g h")
        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{hvezda}", end="")
            else:
                print(f"{tlucka}", end="")
        print()
        
        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{tlucka}", end="")
            else:
                print(f"{hvezda}", end="")
        print()
        
        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{hvezda}", end="")
            else:
                print(f"{tlucka}", end="")
        print()
        
        
        for i in range(1, p + 1):
            print(f"{tlucka}", end="")
        print()

        for i in range(1, p + 1):
            print(f"{tlucka}", end="")
        print()
        
        
        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{nula}", end="")
            else:
                print(f"{tlucka}", end="")
        print()

        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{tlucka}", end="")
            else:
                print(f"{nula}", end="")
        print()
        
        for i in range(1, p + 1):
            if i % 2 == 0:
                print(f"{nula}", end="")
            else:
                print(f"{tlucka}", end="")
        print()
        print("a b c d e f g h")
hvezda = "* "
tlucka = ". "
nula = "o "
p = 8
pocatecny_stav(p)