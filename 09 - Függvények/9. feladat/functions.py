from consolio import *

def hufToJpy(amount:float, exchangeRate:float, jpy:float)->float:
    exchangeRate:float=0.3869
    jpy:float=amount*exchangeRate
    return jpy

def hufToUsd(amount:float, exchangeRate:float, usd:float)->float:
    exchangeRate:float=0.0028
    usd:float=amount*exchangeRate
    return usd

def hufToChf(amount:float, exchangeRate:float, chf:float)->float:
    exchangeRate:float=0.0026
    chf:float=amount*exchangeRate
    return chf

def jpyToEur(jpy:float, eur:float, exchangeRate:float, amount:float)->float:
    exchangeRate:float=0.75
    jpy:float=hufToJpy(amount, exchangeRate, jpy)
    eur=exchangeRate*jpy
    return eur