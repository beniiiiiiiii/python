maximum:int=None
temp:str=None
maxTemp:str=None
number:str=None
osszeg:int=0
db:int=0

print("Kérem adjon meg egy maximum értéket") #ujra nem jo. minden a whileon belul van#
maximum=int(input())

while (osszeg<maximum):
    
    print("Kérek egy számot")
    temp=input()
    if (temp.isnumeric()):
        number=int(temp)
    osszeg+=number
    db+=1
    print(f"A számok összege: {osszeg}")
    print(f"Próbálkozások száma: {db}")
if osszeg>=maximum:
    print(f"{db} lépésben érte el a megadott határértéket")