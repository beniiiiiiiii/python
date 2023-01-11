startVal:int=None
endVal:int=None
five:int=0
seven:int=0


print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal+1, 1):
    if i%5==0 and i%7==0:
        five +=1
        seven +=1
    
    if i%5==0:
        five +=i
    elif i%7==0:
        seven +=i

print(five)
print(seven)

if five>seven:
    print("Az 5-tel osztható számok számok összege nagyobb")
elif seven>five:
    print("A héttel osztható számok összege nagyobb")
else:
    print("Az összegük egyenlő")
