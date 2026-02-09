def mix_columns(state):
    # AES opera sobre una matriz de 4x4 bytes llamada "State".
    # Este bucle recorre cada una de las 4 columnas de forma independiente.
    for col in range(4):
        # 1. Extracción de los bytes actuales de la columna (filas 0 a 3).
        s0 = state[0][col]
        s1 = state[1][col]
        s2 = state[2][col]
        s3 = state[3][col]
        
        # 2. Multiplicación por 2 en el Campo de Galois GF(2^8).
        # En AES, multiplicar por 2 no es un simple desplazamiento. 
        # Si el bit más significativo (0x80) está activo, se aplica un XOR con 0x1b 
        # (el polinomio irreducible) para mantener el resultado dentro de 1 byte.
        mul2_0 = ((s0 << 1) ^ (0x1b if s0 & 0x80 else 0)) & 0xff
        mul2_1 = ((s1 << 1) ^ (0x1b if s1 & 0x80 else 0)) & 0xff
        mul2_2 = ((s2 << 1) ^ (0x1b if s2 & 0x80 else 0)) & 0xff
        mul2_3 = ((s3 << 1) ^ (0x1b if s3 & 0x80 else 0)) & 0xff
        
        # 3. Multiplicación por 3 en GF(2^8).
        # Matemáticamente, (x * 3) es lo mismo que (x * 2) ^ x en este campo.
        # Aprovechamos el resultado de mul2 y le sumamos (XOR) el valor original.
        mul3_0 = mul2_0 ^ s0
        mul3_1 = mul2_1 ^ s1
        mul3_2 = mul2_2 ^ s2
        mul3_3 = mul2_3 ^ s3
        
        # 4. Combinación Lineal (Multiplicación de la matriz de la columna).
        # Cada nuevo byte de la fila es una combinación específica de los bytes de la columna.
        
        
        # Nuevo s0 = (s0*2) XOR (s1*3) XOR s2 XOR s3
        state[0][col] = mul2_0 ^ mul3_1 ^ s2 ^ s3
        
        # Nuevo s1 = s0 XOR (s1*2) XOR (s2*3) XOR s3
        state[1][col] = s0 ^ mul2_1 ^ mul3_2 ^ s3
        
        # Nuevo s2 = s0 XOR s1 XOR (s2*2) XOR (s3*3)
        state[2][col] = s0 ^ s1 ^ mul2_2 ^ mul3_3
        
        # Nuevo s3 = (s0*3) XOR s1 XOR s2 XOR (s3*2)
        state[3][col] = mul3_0 ^ s1 ^ s2 ^ mul2_3

