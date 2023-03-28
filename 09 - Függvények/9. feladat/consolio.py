def getHufAmount()->float:
    huf:int=None
    temp:str=None
    isnumber:bool=False
    truncatedString:str=None

    while(huf==None):
        print("Adja meg a magyar Forint mennyiségét: ", end="")
        temp=input()
        truncatedString=temp.replace(".", "").replace("-", "")
        isnumber=truncatedString.isnumeric()

        if isnumber:
            huf=float(temp)
        else:
            print("Nem számot adott meg")
    return huf