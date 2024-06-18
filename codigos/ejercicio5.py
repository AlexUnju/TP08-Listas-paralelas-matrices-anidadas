def suma_fc_mat(tabla, c, k):
    if c == 'f':
        # Sumar una fila
        suma = 0
        for elemento in tabla[k]:
            suma += elemento
        return suma
    elif c == 'c':
        # Sumar una columna
        suma = 0
        for fila in tabla:
            suma += fila[k]
        return suma
    else:
        print("Error: El segundo argumento debe ser 'f' (fila) o 'c' (columna).")

# Ejemplo de uso:
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sumar la fila 1 (índice 0)
suma_fila = suma_fc_mat(matriz, 'f', 0)
print(f"Suma de la fila 1: {suma_fila}")

# Sumar la columna 2 (índice 1)
suma_columna = suma_fc_mat(matriz, 'c', 1)
print(f"Suma de la columna 2: {suma_columna}")
