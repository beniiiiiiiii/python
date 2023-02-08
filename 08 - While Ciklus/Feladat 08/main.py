drinks:int=None

print("1--Coca Cola\n2--Sprite\n3--Fanta\n4--Fuze Tea\n5--Kinley")

while (drinks==None):
    print("Válasszon egy udítőt!")
    drinks=int(input())
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
        case 6:
            print("Nem választott üdítőt")