temp:str=None
number:str=None
osszeg:int=0
db:int=0

while (osszeg<100):
    print("Kérek egy számot")
    temp=input()
    if (temp.isnumeric()):
        number=int(temp)
    osszeg+=number
    db+=1
    print(f"A számok összege: {osszeg}")
    print(f"Próbák száma: {db}")
if (osszeg>=100):
    print("A számok összege elérte a 100-at")