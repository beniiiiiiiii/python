temp:str=None
drinks:int=None

print("1--Coca Cola\n2--Sprite\n3--Fanta\n4--Fuze Tea\n5--Kinley")

while (drinks==None):
    print("Válasszon egy udítőt!")
    temp=input()
    if (temp.isnumeric()):
        drinks=int(temp)
    
        
 #meg kell nézni h szam e#
    
if(drinks>=1 and drinks<=5):
    match drinks:
        case 1:
            print("Coca Colát Választott")
        case 2:
            print("Spriteot választott")
        case 3:
            print("Fanta Választott")
        case 4:
            print("Fuze Tea Választott")
        case 5:
            print("Kinley-t Választott")
elif(drinks>=6):
    print("Ilyen szám alatt nincs üdítőnk!")