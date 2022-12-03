# Projekt neve: Sajat_nev_gyakorlas

sorozat = [-3, 5, 11, -2, 4]


def sorozatfuggveny(sep=" "):

    numbers = ""

    i = 0
    while i < len(sorozat):
        if i == len(sorozat) - 1:
            numbers += str(sorozat[i])
        else:
            numbers += str(sorozat[i]) + sep + " "
        i += 1
    print(numbers)
    print("______________________________\n")

# 1 A tömb első eleméhez adj egy véletlenszámot a [5; 12] intervallumból!
def randomnum():
    import random
    print("1.1 véletlenszám \n")

    num = int(random.random() * 5 ) + 7
    elso = sorozat[0]
    sorozat[0] = elso + num

    print(f"Véletlen szám: {num} + {elso} = {sorozat[0]}")
    print(sorozat)
    print("______________________________\n")


# 2 Az utolsó elem értékét kérd be, ez páratlan hárommal osztható kéjegyű szám legyen!
# Ha nem ilyen számot adnak meg, akkor addig folytassa a program a bekérést, amíg megfelelő nem lesz a bekért szám!
# A bekéréshez készíts külön függvényt!
def lastone():
    print("1.2 bekérés\n")
    num = int(input("Adj meg egy páratlan, hárommal osztható, kétjegyű számot!"))
    while num % 3 != 0 or num % 2 == 0 or num < 10 or num > 99:
        num = int(input("páratlan, 3-mal osztható kétjegyű számot adj meg! "))
    sorozat.append(num)
    print(sorozat)
    print("______________________________\n")



# 3 Használd a 2. feladat kiíró metódusát paraméter nélkül, ekkor szóközzel írja ki a tömb elemeit, egymás mellé!
def kiiras():
    print("1.3 kiíró paraméter nélkül\n")
    sorozatfuggveny()


# 4 Add meg az első kétjegyű szám helyét és értékét a tömbből!
def first():
    print("1.4 Az első kétjegyű szám: ")
    i = 0

    while sorozat[i] < 10 or sorozat[i] > 99:
        i += 1

    if i >= len(sorozat):
        print("A sorozatban nincs kétjegyű szám. :(")
    else:
        print(f"{sorozat[i]}\n")

    print("______________________________\n")


# 5 Számold meg, hogy hány prímszám van a tömbben! Ehhez készíts külön függvényt, ami eldönti, hogy a paraméterében
# kapott szám prímszám-e?
def prime(szam):
    import math
    prim = True
    oszto = 2
    szam = math.fabs(szam)

    while oszto < szam and (szam % oszto != 0):
        oszto += 1

    if oszto < szam:
        prim = False

    return prim


def prim_db():
    print("1.5 hány db prímszám van\n")

    i = 0
    db = 0

    while i < len(sorozat):
        szam = sorozat[i]
        if prime(szam):
            db += 1
        i += 1
    print(f"{db} db prímszám található a listában")
    print("______________________________\n")
