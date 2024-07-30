import random
dificultad=0
print("elija la dificultad, 1 para Fácil, 2 para Normal, 3 para Difícil")
dificultad=int(input())
if dificultad==1:
        def an():
            nums=random.randint(1,10)
            vidas=5
            nu=0
            print("adivine el número del 1 al 10, tienes 5 vidas")
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
                        print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo fácil")
                        break
            else:
                print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo fácil")
            if vidas==0:
                print("te quedaste sin vidas *inserte sonido de game over*")
            else:
                print("GG")
else: 
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
                    print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo normal")
                    break
        else:
            print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo normal")
        if vidas==0:
            print("te quedaste sin vidas *inserte sonido de game over*")
        else:
            print("GG")
if dificultad==3:
        def an():
            nums=random.randint(1,100)
            vidas=8
            nu=0
            print("adivine el número del 1 al 100, tienes 8 vidas")
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
                        print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo difícil")
                        break
            else:
                print("felicidades, adivinaste el número con",vidas,"vidas restantes en modo difícil")
            if vidas==0:
                print("te quedaste sin vidas *inserte sonido de game over*")
            else:
                print("GG")
an()