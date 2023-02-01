number:int=None
temp:str=None
isnumber:bool=False
truncatedString:str=None

while(number==None or (number<0 or number>9)):
    print("Adjon meg egy számot: ", end="")
    temp=input()
    truncatedString=temp.replace(".", "").replace("-", "")
    isnumber=truncatedString.isnumeric()

    if isnumber:
        number=float(temp)
    else:
        print("Nem számot adott meg")