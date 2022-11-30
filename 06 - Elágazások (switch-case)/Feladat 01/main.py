day:int=None

print("Kérem adja meg hanyadik nap van ebben a hétben")
day=int(input())

match day:
    case 1:
        print("Hétfő")
    case 2:
        print("Kedd")
    case 3:
        print("Szerda")
    case 4:
        print("Csütörtök")
    case 5:
        print("Péntek")
    case 6:
        print("Szombat")
    case 7:
        print("Vasárnap")
    case _:
        print("Nincs ilyen nap")