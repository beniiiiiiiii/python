from os import system
system("cls")

def udvozles(nev:str)->None:
    print(f"Üdvözlöm {nev}")

nev:str=None

print("Kérem adja meg a nevét")
nev=str(input())

udvozles(nev)