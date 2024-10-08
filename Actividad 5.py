#Recorre cada letra del mensaje
def cifCesar(mens,desp):
    res=""
#Convierte la letra a código ASCII
    for i in mens:
        codascii= ord(i)
#Aplica el desplazamiento
        ncod=codascii+desp
#Se asegura que la letra se encuentre entre la "a" y la "z"
        if codascii>96 and codascii<123:
            if ncod>122:
#Si se pasa de "z" vuelve a "a"
                ncod-=26
            elif ncod<97:
#Si es antes de "a" vuelve a "z"
                ncod+=26
#Agrega la letra cifrada al resultado
        res+=chr(ncod)
#Devuelve la cadena cifrada o descifrada
    return res
#Ejemplo
mens="hola"
desp=2
#Cifra el ejemplo
mens_cif=cifCesar(mens,desp)
print(mens_cif)