def feladat1():
    a:int=int(input("Adja meg egy pozitív egész számot"))
    i=1
    while i<=a:
        print(i,end=",")
        i+=1
def feladat2():
    szam:int=int(input("Adj meg egy pozitív egész számot"))
    oszto = 1
    osszeg = 0

    print(f"{szam} osztói:",end="")
    while oszto <=szam:
        if szam % oszto ==0:
            print(oszto,end=",")
            osszeg+=oszto
        oszto +=1
    print("\nOsztók összege:", osszeg)


def felaadat3():
    a:int=int(input("Adj meg egy pozitív egséz számot"))
    b:int=int(input("Adj meg egy pozitív egész számot"))
    c=a
    while c<=b:
        if c% 2 ==0:
            print(c)
        c+=1








