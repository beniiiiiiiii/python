import math

# feladat.py

# 1. feladat
# Készítsen függvényt nagyobb néven
# A függvény bemeneti paramétere két egész szám
# A függvény egész számot adjon vissza
# A függvény térjen vissza a két szám közül a nagyobbikkal

def nagyobb(szam1:int, szam2:int)->int:
    if szam1>szam2:
        return szam1
    elif szam2>szam1:
        return szam2
    else:
        print("egyenlőek")



# Tesztelje a függvényt a következő paraméterekkel: (5,3), (3,5), (3,3)
print("1. feladat")
eredmeny1=nagyobb(5,3)
print(eredmeny1)

eredmeny2=nagyobb(3,5)
print(eredmeny2)

eredmeny3=nagyobb(5,5)
print(eredmeny3)
# 2. feladat
# Készítsen függvényt osszeg néven
# A függvény bemeneti paramétere két egész szám
# A függvény egész számot adjon vissza
# A függvény térjen vissza a két szám összegével
def osszeg(a:int, b:int)->int:
    kimenet:int=a+b
    return kimenet
# Tesztelje a függvényt a következő paraméterekkel: (5,3), (-3,-5), (3,-5)
print("2. feladat")
eredmeny1=osszeg(5,3)
print(eredmeny1)

eredmeny2=osszeg(-3,-5)
print(eredmeny2)

eredmeny3=osszeg(3,-5)
print(eredmeny3)
# 3. feladat
# Készítsen függvényt a téglalap területének meghatározására
# A függvény neve legyen teglalap_terulet
# A függvény bemeneti paramétere két valós szám, a téglalap oldalai
# A függvény valós számot adjon vissza
# Ha a téglalapnak nem értelmezhető a területe térjen vissza a None értékkel
def teglalap_terulet(a:float, b:float)->float:
    if a<=0 or b<=0:
        return None
    else:
        terulet:float=a*b
        return terulet
    
# Tesztelje a függvényt a következő paraméterekkel: (5.3, 2.8), (0, 10), (-10,0)
print("3. feladat")
eredmeny1=teglalap_terulet(5.3,2.8)
print(eredmeny1)

eredmeny2=teglalap_terulet(0,10)
print(eredmeny2)

eredmeny3=teglalap_terulet(-10,0)
print(eredmeny3)
# 4. feladat
# Készítsen függvényt a kör területének meghatározására
# A függvény neve legyen kor_terulet
# A függvény bemeneti paramétere egy valós szám, a kör sugara
# A függvény valós számot adjon vissza
# Ha a kör területe nem értelmezhető a területe térjen vissza a None értékkel
def kor_terulet(sugar:float)->float:
    if sugar<=0:
        return None
    else:
        terulet:float=sugar*math.pi
        return terulet
# Tesztelje a függvényt a következő paraméterekkel: 5.38, 0, -10
print("4. feladat")
eredmeny1=kor_terulet(5.38)
print(eredmeny1)
eredmeny2=kor_terulet(0)
print(eredmeny2)
eredmeny3=kor_terulet(-10)
print(eredmeny3)