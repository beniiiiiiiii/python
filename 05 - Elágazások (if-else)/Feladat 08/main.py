num1:int=None

print("Kérek egy számot")
num1=int(input())

if (num1 % 4 ==0 and num1 % 6 == 0):
    print("Ez a szám osztható 4-el és 6-al")
elif(num1 % 4 == 0):
    print("Ez a szám osztható 4-el")
elif(num1%6==0):
    print("Ez a szám 6-al osztható")
else:
    print("Ez a szám egyikkel se osztható")