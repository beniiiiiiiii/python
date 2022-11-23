from cmath import sqrt
import math
from re import S
import sys


a:int=int(input("kérem az a értéket"))
b:int=int(input("Kérem a b értéket"))
c:int=int(input("Kérem a c értéket"))
x=-2*a

gyoke:int=math.pow(b,2)-4*a*c

if gyoke<0:
    print("Nincs értelme")
    sys.exit()

d:float=math.sqrt(gyoke)

x1:float=(-b-d)/(2*a)
x2:float=(-b+d)/(2*a)

if x1!=x and x2!=x:
    print(f"{x1} {x2}")
elif x1==x and x2!=x:
    print(f"{x2}")
elif x2==x and x1!=x:
    print(F"{x1}")