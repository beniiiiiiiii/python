from consolio import *
from functions import *

word1:str=None
word2:str=None
count:int=None

word1:str=stringInput1(word1)
word2:str=stringInput2(word2)
count:int=stringCompare(word1, word2)

printToConsole(word1, word2, count)
