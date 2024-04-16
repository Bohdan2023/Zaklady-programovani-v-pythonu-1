'''
n=20
for i in range(1,n+1):
    print(i)
'''
'''
i=5
for i in range(10):
    print(i)
'''

'''
n=10

pocet_delitelu = 0
for i in range(1,n+1):
    if n % i == 0:
        pocet_delitelu = pocet_delitelu + 1
je_prvocislo = pocet_delitelu == 2
print(je_prvocislo)
'''
'''
n = 10
for i in range(1, n + 1):
        if (i % 2 == 0 and i % 3 == 0 and i % 4 == 0 and i % 5 == 0 and i % 6 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0):
            print(f"\t{i}", end = " ")
print("")
'''
'''
n=10
je_prvocislo = True
for i in range(1,n + 1):
     if n % i == 0:
        je_prvocislo = False
        print(f"\t{i}", end = " ")
print("")
'''
cislo = 100

prvocislo = True
for i in range(3, cislo + 1):
    if cislo % i == 0:
        prvocislo = False

if prvocislo:
    print(f"{cislo}")

for i in range(1, cislo + 1):
    for x in range(2, int(i ** 0.5) + 1):
        if i % x == 0:
            break
    else:
        if i + 2 <= 100 and all((i + 2) % p != 0 for p in range(2, i)):
            print(f"({i}, {i + 2})")
