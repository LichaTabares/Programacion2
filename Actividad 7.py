import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ni='Imagen_gris.jpg'

imagen= Image.open(ni).convert('L')

matriz=np.array(imagen)

filas=len(matriz)
columnas=len(matriz[0])
aux=0
plt.subplot(1,2,1)
plt.imshow(matriz, cmap='gray')
plt.title("original")

matriz_volteada=np.array(matriz)
for i in range(filas):
    for j in range (int(columnas/2)):
        aux=matriz_volteada[i][j]
        matriz_volteada[i][j]=matriz_volteada[i][columnas-1-j]
        matriz_volteada[i][columnas-1-j]=aux

plt.subplot(1,2,2)
plt.imshow(matriz_volteada, cmap='gray')
plt.title("volteada")

plt.show()