maximum:int=None
temp:str=None
number:str=None
osszeg:int=0
db:int=0

print("Kérem adjon meg egy maximum értéket")
maximum=int(input())

if(maximum>=100):
    while (osszeg<maximum):
        print("Kérek egy számot")
        temp=input()
        temp.isnumeric()
        number=int(temp)
        osszeg+=number
        db+=1
        print(f"A számok összege: {osszeg}")
        print(f"Próbálkozások száma: {db}")
if osszeg>=maximum:
    print(f"{db} lépésben érte el a megadott határértéket")