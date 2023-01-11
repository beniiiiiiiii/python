startVal:int=None
endVal:int=None
sum:int=0


print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal+1, 1):
    if i%2!=0 and i%3==0:
        sum +=1
print(sum)


