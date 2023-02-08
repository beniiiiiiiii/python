numberSmall:int=None
numberBig:int=None
tempSmall:str=None
tempBig:str=None

while(numberSmall==None or numberBig==None or numberSmall>=numberBig):
    print("Kérek egy számot")
    tempSmall=input()
    print("Kérek egy másik számot")
    tempBig=input()
    if(tempSmall.isnumeric() and tempBig.isnumeric()):
        numberSmall=int(tempSmall)
        numberBig=int(tempBig)

print("Számok:")

for i in range(numberBig, numberSmall-1,-1):
    print(i)