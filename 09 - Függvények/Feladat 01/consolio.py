def getNumberFromConsol()->float:
    number:int=None
    temp:str=None
    isnumber:bool=False
    truncatedString:str=None

    while(number==None):
        print("Adjon meg egy számot: ", end="")
        temp=input()
        truncatedString=temp.replace(".", "").replace("-", "")
        isnumber=truncatedString.isnumeric()

        if isnumber:
            number=float(temp)
        else:
            print("Nem számot adott meg")
    return number

def printToConsole(a:float, b:float, result:float, operator:str)->None:
    print(f"{a} {operator} {b} = {result}")
