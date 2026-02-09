# -PARTE 4: ADDROUNDKEY 

def add_round_key(A, B):
    # 'A' suele ser la matriz de estado ( datos actuales)
    # 'B' es la sub-llave de la ronda actual generada por AES
    
    # Paso 1: Crear la lista que contendrá la matriz final
    resultado = []
    
    # Paso 2: Recorrer cada fila (i) de la matriz A
    # Usamos len(A) para que el código sea flexible a cualquier tamaño
    for i in range(len(A)):
        
        # Paso 3: Crear una lista vacía para la fila que estamos procesando
        fila = []
        
        # Paso 4: Recorrer cada columna (j) dentro de la fila actual
        # len(A[0]) nos da el número de columnas
        for j in range(len(A[0])):
            
            #  LA OPERACIÓN XOR (^) 
            # En criptografía simétrica, el XOR es el rey.
            # Se compara el bit del dato con el bit de la llave.
            # Si son diferentes da 1, si son iguales da 0.
            # Es una suma binaria sin acarreo.
            valor = A[i][j] ^ B[i][j]
            
            # Guardamos el resultado del XOR en nuestra fila temporal
            fila.append(valor)
            
        # Una vez terminada la fila, la añadimos a la matriz resultado
        resultado.append(fila)
        
    # Devolvemos la matriz ya "cifrada" con la llave de esta ronda
    return resultado