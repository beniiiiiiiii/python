from os import system
system("cls")

def muveletek(x:float, y:float)->float:
    osszeg:float=x+y
    kulombseg1:float=x-y
    kulombseg2:float=y-x
    szorzat:float=x*y
    hanyados1:float=x/y
    hanyados2:float=y/x

    return osszeg, kulombseg1, kulombseg2, szorzat, hanyados1, hanyados2

x:float=10
y:float=4

eredmeny:float=muveletek(x,y)
print(f"{x} és {y}-al való műveletek eredményei: {eredmeny}")
