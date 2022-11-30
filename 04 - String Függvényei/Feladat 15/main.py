from os import system

valasztas1:int=None
valasztas2:int=None
valasztas3:int=None

zoldsegLeves:bool=False
husLeves:bool=False
gyumolcsLeves:bool=False

print("Válasszon előételt")
print("1 - Zöldségleves")
print("2 - Húsleves")
print("3 - Gyümölcsleves")
valasztas1=int(input())

if valasztas1==1:
    zoldsegLeves=True
    print("Egy adag zöldségleves")
elif valasztas1==2:
    husLeves=True
    print("Egy adag húsleves")
elif valasztas1==3:
    gyumolcsLeves=True
    print("Egy adag gyümölcsleves")
else:
    print("No előétel?")

sultCsirkecomb:bool=False
sultCsirke:bool=False
rakottZoldseg:bool=False
spagetti:bool=False
pizza:bool=False

print("Válasszon főételt")
print("1 - Sült csirke comb")
print("2 - Sült csirkemell")
print("3 - Rakottzöldség")
print("4 - Spagetti")
print("5 - pizza")
valasztas2=int(input())

if valasztas2==1:
    sultCsirkecomb=True
    print("Egy sült csirkecomb")
elif valasztas2==2:
    sultCsirke=True
    print("Egy sültcsirkemell")
elif valasztas2==3:
    









rizs:bool=False
paroltZoldseg:bool=False
gyumolcs:bool=False
sultKrumpli:bool=False
salata:bool=False
kola:bool=False

