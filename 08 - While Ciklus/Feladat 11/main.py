from random import randint

firstNumber:int=None
secondNumber:int=None
random:int=None
count1:int=0
count2:int=0
average:float=None
db:int=0

while(firstNumber==None and secondNumber==None and random==firstNumber and random==secondNumber):
    print("Kérem adjon meg egy páros számot")
    firstNumber=int(input())
    print("Kérem adjon meg egy páratlan számot")
    secondNumber=int(input())
    random=randint(firstNumber, secondNumber)
    print(random)
    
    for i in range(firstNumber, random, 1):
        count1+=1
    print(f"A páros szám és a random szám közti táv:{count1}")

    for j in range(random, secondNumber, 1):
        count2+=1
    print(f"A páratlan szám és a random szám közti táv:{count2}")

    if (count1>count2):
        print("A véletlen szám a páros számtól van messzebb")
    else:
        print("A véletlen szám a páratlan számtól van messzebb")
    
    average=(firstNumber+secondNumber)/2
    for k in range(firstNumber, secondNumber+1, 1):
        if (k%4==0):
            db+=1
    print(f"A 4-el osztható számok száma: {db}")
