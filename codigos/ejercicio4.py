import os
os.system('cls')

#Realizar los recorridos de las siguientes matrices de NxN, donde N es par, tal como se indica en las siguientes figuras:

matriz=[[1,9,2],[2,4,4],[3,11,5]]

#a (por columnas))

for j in range(len(matriz)):
    for i in range(len(matriz)):
        print(f'Columna {j+1}, fila {i+1}: {matriz[i][j]}')
        
#b (por filas))

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f'Fila {i+1}, Columna {j+1}: {matriz[i][j]}')

#c (recorrido raro))

'''matriz_2 = [[0,3,3,1,9,2],
            [2,1,1,2,4,4],
            [3,11,5,40,23,14],
            [2,22,53,25,30,12],
            [5,55,23,40,90,34],
            [150,21,17,13,7,70]
            ]

long_col=len(matriz_2)//2
long_fil=len(matriz_2)
for j in range(long_col-1,-1,-1):
    for i in range(long_fil-1,-1,-1):
        print(matriz_2[i][j])
    for k in range(long_col-1,-1,-1):
        print(matriz_2[i][k])
    print()'''
    
matriz_2 = [
    [0, 3, 3, 1, 9, 2],
    [2, 1, 1, 2, 4, 4],
    [3, 11, 5, 40, 23, 14],
    [2, 22, 53, 25, 30, 12],
    [5, 55, 23, 40, 90, 34],
    [150, 21, 17, 13, 7, 70],
]

long_col = len(matriz_2) // 2
long_fil = len(matriz_2)
final_row = long_fil + 1

# Itera en la columna
for j in range(long_col - 1, -1, -1):
    # Itera subiendo de fila en fila
    for i in range(1, final_row + 1):
        # Verifica si esta en la ultima columna para empezar a contar hacia el lado izquierdo
        if i >= final_row:
            # Resta 1 espacio en la fila, al fin y al cabo no queremos un error de list out of index
            i -= 1
            # Itera en reversa por la diferencia de final_row y long_fil dandonos las casillas que deberia iterar por columna
            for n in range(final_row - long_fil, -1, -1):
                print(matriz_2[-i][n])
            break
        print(matriz_2[-i][j])

    # Elimina 1 fila para la siguiente iteración de columna
    final_row -= 1