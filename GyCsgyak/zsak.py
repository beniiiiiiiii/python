import random

gyujtok:int=None
fogyaszt:int=None
zsak:int=20



while(zsak>0):
    gyujtok=random.randint(0,5)
    fogyaszt=random.randint(0,10)
    zsak-=fogyaszt
    zsak+=gyujtok
    print(zsak)
    if (gyujtok>fogyaszt):
        print(f"gyujtők: {gyujtok}")
    elif(gyujtok<fogyaszt):
        print(f"fogyasztók: {fogyaszt}")
    else:
        print("=======================")

        