def feladat1():
    print("1. feladat")
    print("Írjuk ki 0-tól 150-ig a páros számokat!")
    szam: int = 0
    while szam <= 150:
        if szam < 150:
            print(szam, end = "; ")
        else:
            print(szam, end = " ")      
        szam += 2

def feladat2():
    print("\n")
    print("2. feladat")
    print("Számold meg 10 bekért szám esetében a 3-mal osztható számokat!")
    szamokszama = 0    
    harommaloszthato = 0     

    while szamokszama < 10:
        bekertszamok:int = int(input("Adjon meg egy számot: "))
        szamokszama += 1
        if bekertszamok % 3 == 0:
            harommaloszthato += 1

    print("A számok közül ennyi osztható hárommal: " + str(harommaloszthato))

def feladat3():
    print("\n")
    print("3. feladat")
    print("Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!") 
    szambekeres:int = int(input("Adjon meg egy 10-zel osztható számot: "))
    while not(szambekeres % 10 == 0):
                szambekeres:int = int(input("Ez a szám nem osztható 10-zel!!! Adjon meg egy másikat: "))
    print("Végre jó számot adtál meg!")

def feladat4():
    print("\n")
    print("4. feladat")
    print("Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!")
    szambekeres:int = int(input("Adjon meg egy kétjegyű páros számot: "))
    while not((100 > szambekeres >= 10 or (szambekeres <= -10 and szambekeres > -100)) and szambekeres % 2 == 0):
        szambekeres:int = int(input("Ez nem a megfelelő szám! Adjon meg egy újat: "))
    print("Végre jó számot adtál meg!")

def feladat5():
    print("\n")
    print("5. feladat")
    print("Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.")
    szambekeres: int = int(input("Adjon meg egy pozitív páratlan számot: "))
    while not(szambekeres >= 0 and szambekeres % 2 == 1):
        szambekeres:int = int(input("Ez nem megfelelő szám! Adjon meg egy másikat: "))
    print("Végre jó számot adtál meg!")

def feladat6():
    print("\n")
    print("6. feladat")
    print("Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.")
    szambekeres: int = int(input("Adjon meg egy 3-mal osztható számot vagy négyzetszámot: "))
    while not((szambekeres ** 0.5) % 1 == 0 or szambekeres % 3 == 0):
        szambekeres:int = int(input("Ez nem megfelelő szám! Adjon meg egy másikat: "))
    print("Végre jó számot adtál meg!")

def feladat7():
    print("\n")
    print("7. feladat")
    print("Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!")
    szambekeres: int = int(input("Adjon meg egy számot: "))
    szambekeres2: int = int(input("Adjon meg egy számot: "))
    szambekeres3: int = int(input("Adjon meg egy számot: ")) 
    