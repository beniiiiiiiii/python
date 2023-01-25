startVal:int=None
endVal:int=None
sum:int=0
sum2:int=0
solution:int=None


print("Kérem adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

if startVal%2==0:
    startVal-=1

for i in range(startVal, endVal+1):
    if i%2:
        sum +=i
    if i%2==0:
        sum2 +=i

solution=sum-sum2
print(solution)