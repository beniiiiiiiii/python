startVal:int=None
endVal:int=None

print("Adja meg az intervallum kezdő ée vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal, -1):
    print(i)