startVal:int=None
endVal:int=None

print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

if (startVal % 2):
    startVal-=1

for i in range(startVal, endVal, 2):
    print(i)