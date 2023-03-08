maximum:int=None
temp:str=None
maxTemp:str=None
number:int=None
osszeg:int=0
db:int=0

while (maximum==None or maximum<100):#nem jo a while feltetele. nem addig keregeti a szamokat ameddig az osszeg a maximum ertek#
    print("Kérem adjon meg egy maximum értéket")
    maxTemp=input()
    if (maxTemp.isnumeric()):
        maximum=int(maxTemp)

while(number==None and osszeg>=100):
    print("Kérek egy számot")
    temp=input()
    if (temp.isnumeric()):
        number=int(temp)
    osszeg+=number
    db+=1
    print(f"A számok összege: {osszeg}")
    print(f"Próbálkozások száma: {db}")
