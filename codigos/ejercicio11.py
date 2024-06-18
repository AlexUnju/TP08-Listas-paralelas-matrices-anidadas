def transpuesta(m):
    # Obtener las dimensiones de la matriz original
    filas_originales = len(m)
    columnas_originales = len(m[0]) if filas_originales > 0 else 0

    if columnas_originales == 0:
        return []

    # Inicializar la matriz transpuesta
    matriz_transpuesta = []
    for col in range(columnas_originales):
        nueva_fila = []
        for fila in range(filas_originales):
            nueva_fila.append(m[fila][col])
        matriz_transpuesta.append(nueva_fila)

    return matriz_transpuesta

# Ejemplo de uso:
matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado_transpuesta = transpuesta(matriz_original)
print("Matriz original:")
for fila in matriz_original:
    print(fila)
print("\nMatriz transpuesta:")
for fila in resultado_transpuesta:
    print(fila)
