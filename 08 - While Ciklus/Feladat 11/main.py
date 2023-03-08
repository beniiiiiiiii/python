from random import randint

firstNumber:int=None
secondNumber:int=None
random:int=None
firstCount:int=0
secondCount:int=0
average:float=None
db:int=0

while(firstNumber==None and random==firstNumber): #ketto while ismet#
    print("Kérem adjon meg egy páros számot")
    firstNumber=int(input())
while(secondNumber==None and random==secondNumber):
    print("Kérem adjon meg egy páratlan számot")
    secondNumber=int(input())
    random=randint(firstNumber, secondNumber)
    print(random)
    
    for i in range(firstNumber, random, 1):
        firstCount+=1
    print(f"A páros szám és a random szám közti táv:{firstCount}")

    for j in range(random, secondNumber, 1):
        secondCount+=1
    print(f"A páratlan szám és a random szám közti táv:{secondCount}")

    if (firstCount>secondCount):
        print("A véletlen szám a páros számtól van messzebb")
    else:
        print("A véletlen szám a páratlan számtól van messzebb")
    
    average=(firstNumber+secondNumber)/2
    for k in range(firstNumber, secondNumber+1, 1):
        if (k%4==0):
            db+=1
    print(f"A 4-el osztható számok száma: {db}")
