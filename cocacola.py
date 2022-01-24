import random

num=0
x=0
z=""
base="2480655"
max = 9999
min = 1111
range = max - min + 1
achdot = 0
asarot=0
meot=0
alfim=0
i=0
num = input('how much codes you want \n')
num=(int (num))
while num>i:

    x=(random.randint(1111, 9999))
    if x<5555 or x<4555 or x<3555 or x<2555 or x<1555:
        x=str(x)
        base=str(base)
        z=base+x+"5"
        print()
        i+=1
    else:
        achdot = x % 10
        x /= 10
        asarot = x % 10
        x /= 10
        meot = x % 10
        x /= 10
        alfim = x % 10
        x /= 10
        achdot = achdot / 2
        asarot = asarot / 2
        meot = meot / 2
        alfim = alfim / 2
        achdot=round(achdot)
        asarot=round(asarot)
        meot=round(meot)
        alfim=round(alfim)
        achdot= str(achdot)
        asarot= str(asarot)
        meot= str(meot)
        alfim= str(alfim)

        z=base + achdot + asarot + meot + alfim + "5"
        print (int (z))