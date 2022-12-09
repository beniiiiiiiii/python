import math

a:int=None
b:int=None
menu:str=None
eredmeny:float=None

print("Kérem adja meg az a értékét")
a=int(input())
print("Kérem adja meg a b értékét")
b=int(input())
print("Kérem válasszon műveletet: t--terület\n k--kerület\n a--átló")
menu=str(input()).lower().strip()

match menu:
    case "t":
        eredmeny=a*b
        print(eredmeny)
    case "k":
        eredmeny=(a+b)*2
        print(eredmeny)
    case "a": 
        eredmeny=math.sqrt(math.pow(a,2)+math.pow(b,2))
        print(eredmeny)