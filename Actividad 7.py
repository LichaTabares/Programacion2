import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color

#Cargar la image desde un archivo jpg
imagen = io.imread('Imagen gris.jpg')
#Convertimos la imagen a una matriz
matriz= np.array(imagen)
#Mostrar la imagen original y hacer el arreglo para poder mostrar las imágenes una al lado de la otra
plt.subplot(1,2,1)
#Usar el mapa de colores 'gray'para visualizar correctamente
plt.imshow(matriz,cmap='gray')
plt.title('imagen original')

#Voltear la imagen
matriz_volteada = []

#Recorremos cada fila
for i in range (len(matriz)):#len(matriz) nos da el número de filas
#Hacemos una lista vacia para la fila volteada
    filas=[]
#len (matriz[i]) nos da el número de columnas
    for j in range (len(matriz[i])):
#Invertimos las filas
        filas.append(matriz[i][len(matriz[i])-1-j])
    
    #Agregamos la fila volteada a la matriz volteada
    matriz_volteada.append(filas)
    
matriz_volteada=np.array(matriz_volteada)
#Mostrar la imagen volteada y ponerla segunda imagen al lado
plt.subplot(1,2,2)
plt.imshow(matriz_volteada, cmap='gray')
plt.title('imagen volteada')

#Mostrar todo
plt.show()