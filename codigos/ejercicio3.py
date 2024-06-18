import random

def cargar_matriz_cuadrada(n):
    matriz = []
    for i in range(n):
        fila = [random.randint(1, 100) for _ in range(n)]
        matriz.append(fila)
    return matriz

def mostrar_diagonal_principal(matriz):
    print("Valores de la diagonal principal:")
    for i in range(len(matriz)):
        print(matriz[i][i])

# Solicitar al usuario el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz cuadrada (n): "))
while n <= 0:
    print("El tamaño de la matriz debe ser mayor que cero.")
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n): "))

# Generar la matriz aleatoria
matriz = cargar_matriz_cuadrada(n)

# Mostrar la matriz generada
print("\nMatriz generada aleatoriamente:")
for fila in matriz:
    print(fila)

# Mostrar los valores de la diagonal principal
mostrar_diagonal_principal(matriz)
