nNumber:int=None
temp:str=None
osszeg:int=0
osztas:float=0

while(nNumber==None): 
    print("Kérem adjon meg egy pozitív, kérjegyű számot")
    temp=input()
    if (temp.isnumeric and temp.len()==2 and temp>0):#nem jo a .len()#
        nNumber=int(temp)

print("A választott szám és 0 közti páros számok")
for i in range(0, nNumber+1, 2):
    print(i)
print("A választott szám és 0 közti 5-el osztható számok összege:")
for j in range(0, nNumber+1, 5):
    osszeg+=j
    print(j)
print(osszeg)
print("Am választott szám és 0 közti 11-el osztható számok:")
for k in range(0, nNumber+1, 11):
    if(k%11==0):
        osztas+=1
    print(k)
print(osztas)