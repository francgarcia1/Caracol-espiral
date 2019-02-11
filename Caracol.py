def archivo():
    return "Matriz.txt"

def leer_archivo(txt):
    return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(txt).readlines()]]]

print (leer_archivo(archivo()))

def leng(matriz):
    return len(matriz[0])

def recorrer(matriz, dire, i, j, leng):

    print(matriz[i][j])

    if(dire == 1):
        print("1-i:" , i , " j:" , j)
        if((j+1) == leng):
            recorrer(matriz, 2, (i+1), (j), leng-1)
        if((j+1)<=4):
            recorrer(matriz, dire, (i), (j+1), leng)
        else:
            recorrer(matriz, 3, (i), (j), leng)
            
    elif(dire == 2):
        print("2-i:" , i , " j:" , j)
        if((i) == leng):
            recorrer(matriz, 3, (i), (j-1), leng)
        if((i-1)>=0):
            recorrer(matriz, dire, (i-1), (j), leng)
        
    elif(dire == 3):
        print("3-i:" , i , " j:" , j)
        if( j == 0):
            if ((i-1)>=0):
                recorrer(matriz, 4, (i-1), (j), (leng))
        if((j-1)>=0):
            if(j>4):
                recorrer(matriz, dire, (i), (j-2), leng)
            else:
                recorrer(matriz, dire, (i), (j-1), leng)

    elif(dire == 4):
        print("4-i:" , i , " j:" , j)
        if( i == 0):
            if((j+1)<=4):
                recorrer(matriz, 1, (i), (j+1), leng)

        if((i-1)>=0):
            recorrer(matriz, dire, (i-1), (j), leng) 
                   
print(recorrer(leer_archivo(archivo()), 1, 0 , 0, leng(leer_archivo(archivo()))))
##print(recorrido(3, leer_archivo(getArchivo()), 0 , 0, size(leer_archivo(getArchivo()))))
