num1:int=None

print("Kérem adjon meg egy számot")
num1=int(input())

if (num1 >=0 and num1 <= 9):
    print("Ez a szám egyjegyű")

if (num1 >=10 and num1 <= 99):
    print("Ez a szám kétjegyű")

if (num1 >=100 and num1 <= 999):
    print("Ez a szám háromjegyű")