startVal:int=None
endVal:int=None
three:int=0

print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal, ):
    if i%3==0:
        three +=1
print(three)