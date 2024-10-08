M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
suma=0
mult=1
suma2=0
mult2=1
for i in range(4):
    for j in range(4):
        print(M[i][j])
        if (i==j):
            suma=suma+M[i][j]
            mult=mult*M[i][j]
        if (j==3-i):
            suma2=suma2+M[i][j]
            mult2=mult2*M[i][j]
print("la suma en diagonal",suma)
print("la multiplicación en diagonal",mult)
print("la suma en contradiagonal",suma2)
print("la multiplicación en contradiagonal",mult2)