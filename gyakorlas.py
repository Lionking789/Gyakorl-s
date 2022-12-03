import random

sorozat = [-3, 5, 11, -2, 4]
def feladat1(sep):
    szamok = ""

    i = 0
    while i < len(sorozat)-1:
        szamok += str(sorozat[i]) + sep
        i = i + 1

    print(szamok + str(i))


def veletlen():
   velszam= int(random.random()*7) + 5
   print(velszam + sorozat[0])
   sorozat[0] +=velszam
   print(feladat1("*"))



def utolso():
    i = len(sorozat) -1
    print(len(sorozat) -1)

def kiiro():
    szam = int(input("+-mal osztható nem páros kétjegyű szám: "))

    while not ((szam >=10)) and (szam <=99) and







