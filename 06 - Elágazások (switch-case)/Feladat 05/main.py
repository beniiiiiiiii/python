r1:int=None
r2:int=None
resistor:float=None
kapcs:str=None

print("Kérem az első ellenállás mértékét")
r1=int(input())
print("Kérem a második ellenállás mértékét")
r2=int(input())
print("Hogy vannak kapcsolva? soros--S, párhuzamos--P")
kapcs=str(input()).lower().strip()

match kapcs:
    case "p":
        resistor=(r1+r2)/(r1*r2)
        print(resistor)
    case "s":
        resistor=r1+r2
        print(resistor)