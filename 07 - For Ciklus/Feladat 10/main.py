startVal:int=None
endVal:int=None
sum:int=0
product:int=1

print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range (startVal, endVal):
    sum +=i
print(sum)

for i in range(startVal, endVal):
    product*=i
print(product)