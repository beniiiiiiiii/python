savedMoney:float=None
months:int=0

print("Kérem adja meg a pénze mennyiségét")
savedMoney=int(input())

while(savedMoney<100000):
    savedMoney=savedMoney+(savedMoney*0.02)
    months+=1
print(savedMoney)
print(months)