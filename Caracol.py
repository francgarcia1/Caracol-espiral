def getArchivo():
    return "Matriz.txt"

def leer_archivo(txt):
    return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(txt).readlines()]]]

print (leer_archivo(getArchivo()))

def size(matriz):
    return len(matriz[0])

def recorrido(direccion, matriz, i, j, size):

    print(matriz[i][j])

    if(direccion == 1):
        print("D**i:" , i , " j:" , j)
        if((j+1) == size):
            recorrido(2, matriz, (i+1), (j), size-1) 
        recorrido(direccion, matriz, (i), (j+1), size) 
        
    elif(direccion == 2):
        print("A**i:" , i , " j:" , j)
        if((i) == size):
            recorrido(3, matriz, (i), (j-1), size) 
        recorrido(direccion, matriz, (i+1), (j), size) 
        
    elif(direccion == 3):
        print("I**i:" , i , " j:" , j)
        if( j == 0):
            recorrido(4, matriz, (i-1), (j), (size)) 
        recorrido(direccion, matriz, (i), (j-1), size) 

    elif(direccion == 4):
        print("F**i:" , i , " j:" , j)
        if( i == 0):
            recorrido(1, matriz, (i), (j+1), size) 
        recorrido(direccion, matriz, (i-1), (j), size) 
                   
print(recorrido(1, leer_archivo(getArchivo()), 0 , 0, size(leer_archivo(getArchivo()))))
##print(recorrido(3, leer_archivo(getArchivo()), 0 , 0, size(leer_archivo(getArchivo()))))
