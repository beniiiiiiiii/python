name:str=None

while(name==None or len(name)<2):
    print("Kérem adjon meg egy nevét")
    name=input()

    if (name.isalpha()!=True):
        print("Nem nevet adott meg")
        print("Kérem adja meg a nevét újra")
        name=input()
    if(len(name) >=2 and name.isalpha()==True):
        print("Üdvözlöm!")