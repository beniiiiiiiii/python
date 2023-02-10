from random import randint

number=None
temp:str=None
tries:int=0
solution=None

solution=randint(0,9)

while(tries<5):
    print("találja ki a számot")
    temp=input()
    if (temp.isnumeric()):
        number=int(temp)
    else:
        continue
    if (solution==number):
        print("Kitalálta a számot")
    else:
        tries+=1
if tries==5:
    print("Nem nyert")