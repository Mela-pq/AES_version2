# Importación de las partes desarrolladas por el equipo
from parte1 import sub_bytes   # Josue
from Parte2 import shiftRows   # Mel 
from parte3 import mix_columns # Mateo

# FUNCIÓN DE APOYO PARA TU EXAMEN 
def imprimir_matriz(matriz):
    for fila in matriz:
        # Muestra los números en formato hexadecimal profesional ej: 0x19
        print("| " + " | ".join(f"0x{x:02X}" for x in fila) + " |")
    print("-" * 35)

#  PARTE 4: ADDROUNDKEY Josue
def add_round_key(A, B):
    resultado = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            valor = A[i][j] ^ B[i][j]
            fila.append(valor)
        resultado.append(fila)
    return resultado

#  PROGRAMA PRINCIPAL ----------
def main():
    # Matriz de estado inicial del ejercicio
    estado = [
        [0x19, 0x3D, 0xE3, 0xBE],
        [0xA0, 0xF4, 0xE2, 0x2B],
        [0x9A, 0xC6, 0x8D, 0x2A],
        [0xE9, 0xF8, 0x48, 0x08]
    ]

    # Clave de ronda Round Key
    clave = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]

    print("ESTADO INICIAL ")
    imprimir_matriz(estado)

    # 1. SubBytes Josue
    estado = sub_bytes(estado)
    print("DESPUES DE SubBytes ")
    imprimir_matriz(estado)

    # 2. ShiftRows Mel
    estado = shiftRows(estado)
    print("DESPUES DE ShiftRows ")
    imprimir_matriz(estado)

    # 3. MixColumns Mateo
    # La función de Mateo modifica la matriz directamente
    mix_columns(estado)
    print("DESPUES DE MixColumns ")
    imprimir_matriz(estado)

    # 4. AddRoundKey Josue
    estado = add_round_key(estado, clave)
    print("DESPUES DE AddRoundKey RESULTADO FINAL")
    imprimir_matriz(estado)

if __name__ == "__main__":
    main()