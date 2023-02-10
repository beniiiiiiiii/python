from random import randint

diceThrow:int=None
count=0

while(diceThrow!=6):
    diceThrow=randint(1, 6)
    count+=1
    print(diceThrow)
print(f"{count} próbálkozásból lett 6")    