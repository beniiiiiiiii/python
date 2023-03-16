from consolio import *
from typing import *

def stringCompare(word1:str, word2:str)->int:
    count:int=0
    for i in range(0, len(word1)):
        index:int=word2.find(word1[i])
        if index!=-1:
            count+=1
    return count