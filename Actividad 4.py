import random
alumaux=""
alum=[]
o=[]
cant=0
oa=0

print("Ingrese la cantidad de alumnos")
cant=int(input())

for i in range(0,cant):
    print("ingrese el nombre del alumno")
    alumaux=input()
    alum.append(alumaux)
    
for i in range (len(alum)):
    
    oa=random.randint(0,len(alum)-1)
    alumnos=alum[oa]
    o.append(alumnos)
    del alum[oa]
print("el orden de exposición será:")
print (o)