# ==========================================================
# PROYECTO: IMPLEMENTACIÓN DE UNA RONDA AES
# INTEGRANTES: JOSUE, MEL, MATEO
# MATERIA: SEGURIDAD - UIDE
# ==========================================================

from parte1 import sub_bytes
from Parte2 import shiftRows
from parte3 import mix_columns

# FUNCIONES PROPORCIONADAS 

def dimension (matriz):
    filas = len(matriz)
    if filas > 0:
        columnas = len(matriz[0])
    else:
        columnas = 0
    return filas, columnas

def imprimir (A):
    f, c = dimension (A)
    for i in range(0, f):
        print ("| ", end = "") 
        for j in range(0, c):
            # El formato :>5 alinea a la derecha con 5 espacios
            print ("{:>5} |".format(A[i][j]), end = "")
        print("") 

def inicializar (nf, nc):
    A = [] 
    for i in range (nf):
        fila = [0] * nc 
        A.append(fila)           
    return A

# PARTE 4: ADDROUNDKEY JOSUE

def add_round_key(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            valor = A[i][j] ^ B[i][j]
            fila.append(valor)
        resultado.append(fila)
    return resultado

#  PROGRAMA PRINCIPAL 

def main():
    # Estado inicial del ejercicio
    estado = [
        [0x19, 0x3D, 0xE3, 0xBE],
        [0xA0, 0xF4, 0xE2, 0x2B],
        [0x9A, 0xC6, 0x8D, 0x2A],
        [0xE9, 0xF8, 0x48, 0x08]
    ]

    # Clave de la ronda
    clave = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]

    print("ESTADO INICIAL")
    imprimir(estado)

    # 1. SubBytes (Josue)
    estado = sub_bytes(estado)
    print("\nDESPUES DE SubBytes")
    imprimir(estado)

    # 2. ShiftRows (Mel)
    estado = shiftRows(estado)
    print("\nDESPUES DE ShiftRows")
    imprimir(estado)

    # 3. MixColumns (Mateo)
    mix_columns(estado)
    print("\nDESPUES DE MixColumns")
    imprimir(estado)

    # 4. AddRoundKey (Josue)
    estado = add_round_key(estado, clave)
    print("\nDESPUES DE AddRoundKey RESULTADO FINAL")
    imprimir(estado)

if __name__ == "__main__":
    main()