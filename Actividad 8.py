import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ni='Imagencolor.jpg'
imagen=Image.open(ni)
matriz=np.array(imagen)

filas=len(matriz)
columnas=len(matriz[0])
gris=np.zeros(filas, columnas)

for i in range(filas):
    for j in range(columnas):
        r, g, b=matriz[i][j]
        gris[i][j]=int(r * 0.2989 + g * 0.5870 + b * 0.1140)
        matriz[i][j]=[gris, gris, gris]

plt.imshow(matriz, cmap='gray')
plt.title('Imagen en escala de grises')

plt.show()