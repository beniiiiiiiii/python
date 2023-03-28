from functions import *
from consolio import *

amount:float=None
exchangeRate:float=None
jpy:float=None
usd:float=None
chf:float=None
eur:float=None


amount:float=getHufAmount()
jpy:float=hufToJpy(amount, exchangeRate, jpy)
usd:float=hufToUsd(amount, exchangeRate, usd)
chf:float=hufToChf(amount, exchangeRate, chf)
eur:float=jpyToEur(jpy, eur, exchangeRate, amount)
print(usd)
print(jpy)
print(chf)
print(eur)