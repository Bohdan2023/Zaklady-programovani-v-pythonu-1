x = int(input("cislo:"))
d = 2
while (x > 1):
    if (x % d == 0):
       x = x / d
       print(d, end =" ")
    else:
        d = d + 1