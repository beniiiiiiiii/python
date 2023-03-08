month:int=0
number:int=None
osszeg:int=None

print("Adja meg megtakarított pénzének a mennyiseget")
number=int(input())
osszeg=int(number)
while(osszeg<100000):
    osszeg=osszeg*1.02
    month+=1
print(f"{month} hónap múlva éri el az összeg a 100000 Ft-t")
print(f"A végső összeg {osszeg}")