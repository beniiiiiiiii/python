import random
from consolio import *

def elsoJatek():
    szam:int=random.randint(0, 9)
    szamlalo:int=0
    tipp:int=None
    while tipp==None or tipp!=szam:
        print("tippelj pls 0 és 9 közt")
        tipp=getGuessFromConsol()
        szamlalo+=1
        if tipp==szam:
            print(f"ugyes. eltalaltad a szam {szam} volt")
        elif tipp<szam:
            print(f"nem jo. a tipp kisebb mint a szam. próbálkozások: {szamlalo}")
        elif tipp>szam:
            print(f"nem jo. a tipp nagyobb mint a szam. próbálkozások: {szamlalo}")

    
def masodikJatek():
    szam:int=random.randint(40, 50)
    szamlalo:int=0
    tipp:int=None
    while tipp==None or tipp!=szam:
        print("tippelj pls 40 és 50 közt")
        tipp=getGuessFromConsol()
        szamlalo+=1
        if tipp==szam:
            print(f"ugyes. eltalaltad a szam {szam} volt")
        elif tipp<szam:
            print(f"nem jo. a tipp kisebb mint a szam. próbálkozások: {szamlalo}")
        elif tipp>szam:
            print(f"nem jo. a tipp nagyobb mint a szam. próbálkozások: {szamlalo}")


