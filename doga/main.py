startVal:int=None
endVal:int=None
sum:int=0
average:int=0
division:float=0


print("Kérem adja meg a ciklus kezdőértékét")
startVal=int(input())
print("Kérem adja meg a ciklus végértékét")
endVal=int(input())

for i in range(startVal, endVal+1):
    sum +=i
    average=sum/endVal
    if i%3==0:
        division+=i
        print(f"A {startVal} és a {endVal} közti hárommal osztható számok:{i}")

print(f"A {startVal} és a {endVal} közti számok összege: {sum}.")
print(f"A {startVal} és a {endVal} közti számok átlaga: {average}.")