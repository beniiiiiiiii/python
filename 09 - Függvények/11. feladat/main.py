from consolio import *
from functions import *

result=[]
nev:str=None
time:int=None
wage:int=None
overtimeWage:int=0


for i in range(0, 5):
    nev:str=getNameFromConsol(nev)
    time:int=getTimeFromConsol()
    wage:int=calculateWage(wage, time)+calculateOverTimeWage(time, overtimeWage)
    overtimeWage:int=calculateOverTimeWage(time, overtimeWage)
    result.append(storeStr(nev, wage, overtimeWage, time))

for j in result:
    print(j)
