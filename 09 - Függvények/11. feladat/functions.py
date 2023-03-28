from consolio import *

def calculateWage(wage:int, time:int)->int:
    wage:int=None
    if time>40:
         wage=40*1000
    else:
         wage=time * 1000
    return wage

def calculateOverTimeWage(time:int, overtimeWage:int)->int:
    overtimeWage:int=0
    if time>40:
            overtimeWage:int=(time-40) * 1500
    return overtimeWage

def storeStr(nev:str, wage:int, overtimeWage:int, time:int)->None:
    data:str=f"{nev} ezen a héten {time} órát dolgozott.\nA bére: {wage}\nA túlóra extra bére: {overtimeWage}"
    return data