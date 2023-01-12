startVal:int=None
endVal:int=None
sum:int=0
db:int=0
average:float=0

print("Kérem adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal+1, 2):
    sum+=i
    db+=1
    
average=sum/db


print(average)