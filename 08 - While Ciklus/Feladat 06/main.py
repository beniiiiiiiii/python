age:int=None
temp:str=None

while(age==None):
    print("Kérem adjon meg egy életkort")
    temp=int(input())
    if (temp.isnumeric()):
        age=int(temp)

if (age>= 0 and age<=6):
    print("Gyerekkor")
if (age>=7 and age<=18):
    print("iskoláskor")
if (age>=19 and age <=65):
    print("Dolgozókor")
if (age>65):
    print("Nyugdíjas")