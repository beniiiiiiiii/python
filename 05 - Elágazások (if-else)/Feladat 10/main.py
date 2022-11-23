num1:int=None

print("Kérem adjon me egy egész számot")
num1=int(input())

if (num1%2==0 and num1%3==0):
    print("ZIZI")
elif (num1%2==0):
    print("BIZ")
elif (num1%3==0):
    print("BAZ")
else:
    print("EZ a szám nem osztható egyikkel se")
