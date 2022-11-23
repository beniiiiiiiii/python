valasztas:int=None

zoldsegLeves:bool=False
husLeves:bool=False
gyumolcsLeves:bool=False
eloetel:str=None

sultCsirkeComb:bool=False
sultCsirkemell:bool=False
rakottZoldseg:bool=False
spagetti:bool=False
pizza:bool=False
foetel:str=None

rizs:bool=False
paroltZoldseg:bool=False
gyumolcs:bool=False
sultKrumpli:bool=False
salata:bool=False
kola:bool=False
koret:str=None

print("Kérem válasszon előételeink közül:")
print("Zöldségleves -- 1")
print("Húsleves -- 2")
print("gyümölcsleves -- 3")
print("Nincs előétel -- 4")
valasztas=int(input())

if (valasztas == 1):
    zoldsegLeves=True
    eloetel="Zöldségleves"
elif (valasztas==2):
    husLeves==True
    eloetel="húsleves"
elif (valasztas==3):
    gyumolcsLeves=True
    eloetel="gyümölcsleves"
elif (valasztas==4):foeteloetel="Nem választott"

print("Kérem válasszon főételeink közül:")
print("Sültcsirkecomb -- 1")
print("Sült csirkemell -- 2")
print("Rakott zöldség -- 3")
print("Spagetti -- 4")
print("Pizza -- 5")
print("Nincs előétel -- 6")

if (valasztas == 1):
    sultCsirkeComb=True
    foetel="Sültcsirkecomb"
elif (valasztas==2):
    sultCsirkemell==True
    foetel="Sült csirkemell"
elif (valasztas==3):
    rakottZoldseg=True
    foetel="Rakott zöldség"
elif (valasztas==4):
    spagetti=True
    foetel="Spagetti"
elif (valasztas==5):
    pizza=True
    foetel="Pizza"
elif (valasztas==6):
    foetel="Nem választott"

print("Kérem válasszon köreteink közül:")
print("Rizs -- 1")
print("Pároltzsöldség -- 2")
print("Gyümölcs -- 3")
print("Sültkrumoli -- 4")
print("Saláta -- 5")
print("Kóla -- 6")
print("Nincs előétel -- 7")

if (valasztas == 1):
    rizs=True
    koret="Rizs"
elif (valasztas==2):
    paroltZoldseg==True
    koret="Pároltzöldség"
elif (valasztas==3):
    gyumolcs=True
    koret="Gyümölcs"
elif (valasztas==4):
    sultKrumpli=True
    koret="Sültkrumpli"
elif (valasztas==5):
    salata=True
    koret="Saláta"
elif (valasztas==6):
    kola=True
    koret="Kóla"
elif (valasztas==7):
    koret="Nem választott"