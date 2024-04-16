q = int(input("day of year:"))

a,b = 1,31
c,d = 32,59
e,f = 60,90
g,h = 91,120
i,j = 121,151
k,l = 152,181
m,n = 182,212
o,p = 213,243
r,s = 244,274
t,u = 275,304
v,w = 305,334
x,y = 335,365

if (a<=q<=b):
    print("Leden")
elif (c<=q<=d):
    print("Unor")
elif (e<=q<=f):
    print("Brezen")
elif (g<=q<=h):
    print("Duben")
elif (i<=q<=j):
    print("Kveten")
elif (k<=q<=l):
    print("Cerven")
elif (m<=q<=n):
    print("Cervenec")
elif (o<=q<=p):
    print("Srpen")
elif (r<=q<=s):
    print("Zari")
elif (t<=q<=u):
    print("Rijen")
elif (v<=q<=w):
    print("Listopad")
elif (x<=q<=y):
    print("Prosinec")

if (a<=q<=y):
    if (q == 1):
        print('Nedele')
    else:
        result = q % 7
        if result == 2:
            print('Pondeli')
        if result == 3:
            print('Utery')
        if result == 4:
            print('Streda')
        if result == 5:
            print('Ctvrtek')
        if result == 6:
            print('Patek')
        if result == 0:
            print('Sobota')
        if result == 1:
            print('Nedele')