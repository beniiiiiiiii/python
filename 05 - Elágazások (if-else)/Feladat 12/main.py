num1:int=None

print("Kérem adjon meg egy számot")
num1=int(input())

if ((num1 > 10 and num1 < 20) or (num1 > -20 and num1 < -10)):
    print("A szám a tartományon belül van")
else:
    print("A szám nincs a tartományban")