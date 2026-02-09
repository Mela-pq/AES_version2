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
    
    for i in range(len(m)):
        
        fila= m[i]
        
        nueva_fila= fila[i:]+ fila[:i]
        
        nueva_matriz.append(nueva_fila)
        
    return nueva_matriz  
      