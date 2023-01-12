startVal:int=None
endVal:int=None
sumOdd:int=0
sumEven:int=0
db1:int=0
db2:int=0
oddAverage:float=0
evenAverage:int=0

print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal+1, 1):
    if i%2==0:
        sumEven+=i
        db1+=1
    elif i%2:
        sumOdd+=i
        db2+=1

oddAverage=sumOdd/db2
evenAverage=sumEven/db1

print(oddAverage)
print(evenAverage)

if oddAverage>evenAverage:
    print("A páratlan számok átlaga nagyobb")
elif evenAverage>oddAverage:
    print("A páros számok átlaga nagyobb")
else:
    print("Az átlaguk egyenlő")