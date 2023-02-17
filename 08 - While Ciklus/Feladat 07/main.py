numberSmall:int=None
numberBig:int=None
tempSmall:str=None
tempBig:str=None

while(numberSmall==None): #ketto while kell. kuka#
    print("Kérek egy számot")
    tempSmall=input()
    if(tempSmall.isnumeric()):
        numberSmall=int(tempSmall)

while(numberBig==None):
    print("Kérek egy másik számot")
    tempBig=input()
    if(tempBig.isnumeric()):
        numberBig=int(tempBig)
    
print("Számok:")

for i in range(numberBig, numberSmall-1,-1):
    print(i)