startVal:int=None
endVal:int=None
even:int=0
odd:int=0

print("Adja meg az intervallum kezdő és vég értékét")
startVal=int(input())
endVal=int(input())

for i in range(startVal, endVal+1, 1):
    if i%2==0:
        even +=i
    elif i%2!=0:
        odd +=i

print(odd)
print(even)

if even<odd:
    print("A páros számok összege nagyobb")
else:
    print("A páratlan számok összege nagyobb")
