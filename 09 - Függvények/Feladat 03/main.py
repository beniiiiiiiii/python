from os import system
system("cls")

def szuletes(nev:str, kor:int)->int:
    kor:int=2023-kor
    return kor

nev:str=None
kor:int=None

print("Kérem adja meg a nevét")
nev=str(input())
print("Kérem adja meg a születésí évét")
kor=int(input())

szuletes(nev, kor)