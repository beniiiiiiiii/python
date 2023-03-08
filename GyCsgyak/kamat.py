temp:str=None
number:int=0
isNumber:bool=None
month:int=0
osszeg:int=number

while(number<1):
    print("Adja meg megtakarított pénzének a mennyiseget")
    temp=input()
    isNumber=temp.isnumeric()
    if(isNumber):
        number=int(temp)

while(osszeg<100000):
    month+=1
    osszeg=osszeg+(number*0.02)

print(f"{month} hónap múlva éri el az összeg a 100000 Ft-t")
print(f"A végső összeg {osszeg}")