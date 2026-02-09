#Funciones

#Para saber cuantas filas y 
# columnas tiene la matriz.

def dimension (matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

#manera de imprimir  con un diseño .

def imprimir (A):
    f, c = dimension (A)
    for i in range(0, f):
        print ("| ", end = "") # end = "" es para no imprimir un salto de línea al final del print
        for j in range(0, c):
            print ("{:>5} |".format(A[i][j]), end = "")
        print("") #Imprime un salto de línea

#matriz llena de ceros

def inicializar (nf, nc):
    A = [] #Lista vacía
    for i in range (nf):
        fila = [0] * nc # nueva fila
        A.append(fila) # aumente una copia de la fila            
    return A

#ShiftRows: Desplazamiento cíclico de las filas de la matriz.
#cada matriz se desplaza a la izquierda 
#cada fila se mueve una cantidad diferente

#Reglas 

#Matriz 4x4 bytes 

#Fila 0	 No se mueve
#Fila 1	 1 posición a la izquierda
#Fila 2	 2 posiciones a la izquierda
#Fila 3	 3 posiciones a la izquierda
#fila[i:]+ fila[:i] i es el numero o la cantidad
#de movimientos y permite cambiar el orden de la matriz


def shiftRows (m):
    
    nueva_matriz=[]
    
    for i in range(4):
        
        fila= m[i]
        
        nueva_fila= fila[i:]+ fila[:i]
        
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz  
      