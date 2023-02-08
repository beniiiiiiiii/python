number:int=None
temp:str=None

while(number==None or number<99 or number>999 or number%7!=0):
    print("Kérem adjon meg egy háromjegyű számot")
    temp=input()
    if(temp.isnumeric()):
        number=int(temp)
    if(number%7==0):
        print("A szám ozstható 7-el")
    else:
        print("A szám nem osztható 7-el")