def getGuessFromConsol()->float:
    guess:int=None
    temp:str=None
    isnumber:bool=False
    truncatedString:str=None

    while(guess==None):
        print("Adjon meg egy számot: ", end="")
        temp=input()
        truncatedString=temp.replace(".", "").replace("-", "")
        isnumber=truncatedString.isnumeric()

        if isnumber:
            guess=float(temp)
        else:
            print("Nem számot adott meg")
    return guess