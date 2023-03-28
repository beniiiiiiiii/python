def getNameFromConsol(nev:str)->str:
    nev:str=None
    print("Kérem adja meg a nevét")
    nev=str(input())
    return nev

def getTimeFromConsol()->int:
    time:int=None
    temp:str=None
    isnumber:bool=False
    truncatedString:str=None

    while(time==None):
        print("Adja meg hány órát dolgozott a héten: ", end="")
        temp=input()
        truncatedString=temp.replace(".", "").replace("-", "")
        isnumber=truncatedString.isnumeric()

        if isnumber:
            time=float(temp)
        else:
            print("Nem számot adott meg")
    return time

def printToConsol(nev:str, wage:int, overtimeWage:int, time:int)->None:
    print(f"{nev} ezen a héten {time} órát dolgozott.\nA bére: {wage}\nA túlóra extra bére: {overtimeWage}")

