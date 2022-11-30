num1:int=None

print("Kérem adjon meg egy számot")
num1=int(input())

if (num1%2==0 and num1>0 and num1%5!=0):
    print("Ez a szám egy pozitív páros szám ami nem osztható 5-tel")
elif (num1%2==0 and num1<0 and num1%5!=0):
    print("Ez a szám egy negatív páros szám ami nem osztható 5-tel")
elif(num1%2==0 and num1>0 and num1%5==0):
     print("Ez a szám egy pozitív páros szám ami osztható 5-tel")
elif(num1%2==0 and num1<0 and num1%5==0):
    print("Ez a szám egy negatív páros szám ami osztható 5-tel")
elif(num1%2!=0 and num1>0 and num1%5!=0):
    print("Ez a szám egy páratlan pozitív szám ami nem osztható5-tel")
elif(num1%2==0 and num1<0 and num1%5!=0):
    print("Ez a szám egy páratlan negatív szám ami nem osztható 5-tel")