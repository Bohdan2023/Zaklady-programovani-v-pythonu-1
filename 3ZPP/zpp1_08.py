listr = input("x:")
dlist = list(listr)

s_c = {}
s = 0
for s in dlist:
    if s in s_c:
        s_c[s] = s_c[s] + 1
    else:
        s_c[s] = 1
        
for s, count in s_c.items():
    print(f"{s} : {count}")