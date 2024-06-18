def buscar_x_matriz(m, x):
    filas = len(m)
    columnas = len(m[0]) if filas > 0 else 0
    
    for fila in range(filas):
        for columna in range(columnas):
            if m[fila][columna] == x:
                return fila, columna
    return -1, -1  # Retorna -1, -1 si no encuentra el valor x en la matriz

def eliminar_fila_matriz(m, fila):
    del m[fila]

def eliminar_columna_matriz(m, columna):
    for fila in m:
        del fila[columna]

def eliminar_x(m, x):
    fila, columna = buscar_x_matriz(m, x)
    while fila != -1 and columna != -1:
        eliminar_fila_matriz(m, fila)
        eliminar_columna_matriz(m, columna)
        fila, columna = buscar_x_matriz(m, x)

def cargar_matriz():
    # Aquí puedes implementar la carga de la matriz desde el usuario o de manera aleatoria
    # Por ejemplo:
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def mostrar_matriz(m):
    for fila in m:
        print(fila)

def main():
    m = cargar_matriz()
    x = int(input("x: "))
    eliminar_x(m, x)
    print("Matriz después de eliminar filas y columnas con valor", x)
    mostrar_matriz(m)

main()
