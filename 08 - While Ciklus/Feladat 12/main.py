temp:str=None
savedMoney:float=None
months:int=0
#ide egy while#
while(savedMoney==None and savedMoney<=0):
    print("Kérem adja meg a pénze mennyiségét")
    temp=input
    if (temp.isnumeric()):
        savedMoney=int(temp)

while(savedMoney<100000):
    savedMoney=savedMoney+(savedMoney*0.02)
    months+=1
print(savedMoney)
print(months)