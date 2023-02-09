savedMoney:int=None
months:int=0
interest:float=0

print("Kérem adja meg a pénze mennyiségét")
savedMoney=int(input())

while(savedMoney==None and savedMoney<=100000):
    print("Kérem adja meg a pénze mennyiségét")
    savedMoney=int(input())
interest=savedMoney+(savedMoney*0.02)
print(interest)