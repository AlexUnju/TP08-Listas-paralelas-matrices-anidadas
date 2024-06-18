import random

# Función para cargar listas aleatorias
def cargar_listas_aleatorias(n):
    lst1 = []
    lst2 = []
    lst3 = []
    
    for _ in range(n):
        lst1.append(random.randint(0, 10))
        lst2.append(random.uniform(0.0, 10.0))
        lst3.append(random.choice(['A', 'B']))
        
    return lst1, lst2, lst3

# Función para ordenar listas según el orden de 'A' y 'B'
def ordenar_listas(lst1, lst2, lst3):
    # Obtener índices ordenados de 'A' y 'B'
    indices_A = []
    indices_B = []
    
    for i, letra in enumerate(lst3):
        if letra == 'A':
            indices_A.append(i)
        elif letra == 'B':
            indices_B.append(i)
    
    # Crear listas ordenadas
    lst4 = []
    lst5 = []
    lst6 = []
    
    for i in indices_A + indices_B:
        lst4.append(lst1[i])
        lst5.append(lst2[i])
        lst6.append(lst3[i])
    
    return lst4, lst5, lst6

# Cargar listas aleatorias
lst1, lst2, lst3 = cargar_listas_aleatorias(6)

# Mostrar listas iniciales
print("Listas Iniciales:")
print("lst1 =", lst1)
print("lst2 =", lst2)
print("lst3 =", lst3)

# Ordenar listas según el orden de 'A' y 'B'
lst4, lst5, lst6 = ordenar_listas(lst1, lst2, lst3)

# Mostrar listas ordenadas
print("\nListas Ordenadas:")
print("lst4 =", lst4)
print("lst5 =", lst5)
print("lst6 =", lst6)
