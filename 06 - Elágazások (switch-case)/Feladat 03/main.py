drink:int=None

print("1 -- Coca Cola\n2 -- Pepsi\n3 -- Fanta\n4 -- Sprite")

print("Milyen üdítőt kér?")
drink=int(input())

match drink:
    case 1:
        print("Coca Cola")
    case 2:
        print("Pepsi")
    case 3:
        print("Fanta")
    case 4:
        print("Sprite")
    case _:
        print("NO drink?")