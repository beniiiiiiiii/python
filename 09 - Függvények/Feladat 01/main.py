from os import system
system('cls')
from mathfunctions import *
from consolio import *


x:float=None
y:float=None

result:float=None

x=getNumberFromConsol()
y=getNumberFromConsol()

result=szumOfTwoNumbers(x,y)
printToConsole(x,y,result,"+")

result=differenceOfTwoNumbers(x,y)
printToConsole(x,y,result,"-")

result=multiplicationOfTwoNumbers(x,y)
printToConsole(x,y,result,"*")

result=divisionOfTwoNumbers(x,y)
printToConsole(x,y,result,"/")