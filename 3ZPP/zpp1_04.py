'''
result = 1 + 1/2 +1/3 + 1/4
print(result)
'''
'''
from fractions import Fraction
z1 = 1
z2 = Fraction(1,2)
z3 = Fraction(1,3)
z4 = Fraction(1,4)
z5 = z1 + z2 + z3 + z4
print(z5)
'''
'''
from decimal import Decimal
c1 = Decimal(1)
c2 = Decimal(1)/Decimal(2)
c3 = Decimal(1)/Decimal(3)
c4 = Decimal(1)/Decimal(4)
c5 = c1 + c2 + c3 + c4
print(c5)
'''
'''
a = 1
b = 7
c = 12
'''
a = int(input("cislo x**2:"))
b = int(input("cislo x:"))
c = int(input("cislo:"))
D = b**2 - 4*a*c
import math
if D >= 0:
    x1 = (-b + (math.sqrt(D)))/2
    x2 = (-b - (math.sqrt(D)))/2
    print(x1,x2)
else:
    print("x patri do prazdna")