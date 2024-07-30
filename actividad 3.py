import random
def an():
    nums=random.randint(1,20)
    vidas=6
    nu=0
    print("adivine el número del 1 al 20, tienes 6 vidas")
    nu=int(input())
    if nu!=nums:
        if nu>nums:
            print("el número que ingresaste es mayor")
        else:
            print("el número que ingresaste es menor")
        vidas=vidas-1
        while vidas>0:
            print("ingrese otro. Te quedan",vidas,"vidas")
            nu=int(input())
            if nu!=nums:
                if nu>nums:
                    vidas=vidas-1
                    print("el número que ingresaste es mayor")
                else:
                    print("el número que ingresaste es menor")
                    vidas=vidas-1
            else:
                print("felicidades, adivinaste el número con",vidas,"vidas restantes")
                break
    else:
        print("felicidades, adivinaste el número con",vidas,"vidas restantes")
    if vidas==0:
        print("te quedaste sin vidas *inserte sonido de game over*")
    else:
        print("GG")
an()