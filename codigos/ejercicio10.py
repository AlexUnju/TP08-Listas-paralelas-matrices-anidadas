import random

productos = ["Celulares", "Tabletas", "Notebooks"]
años = [2012, 2013, 2014, 2015, 2016]

ventas = []

def cargar_ventas():
    global ventas
    ventas = []
    for _ in range(5):
        fila = []
        for _ in range(3):
            fila.append(random.randint(100, 1000))
        ventas.append(fila)
    print("Ventas cargadas aleatoriamente.")

def mostrar_datos():
    print("\nMatriz de ventas de productos por años:")
    for fila in ventas:
        print(fila)

def encontrar_venta_maxima():
    max_venta = float('-inf')
    año_max = 0
    producto_max = 0

    for i in range(len(ventas)):
        for j in range(len(ventas[0])):
            if ventas[i][j] > max_venta:
                max_venta = ventas[i][j]
                año_max = años[j]
                producto_max = i

    print(f"\nLa venta máxima fue en el año {año_max} y correspondió al producto '{productos[producto_max]}'.")

def insertar_periodo():
    nuevo_periodo = []
    for _ in range(len(productos)):
        nuevo_periodo.append(random.randint(100, 1000))
    ventas.append(nuevo_periodo)
    print(f"\nNuevo período insertado: {nuevo_periodo}")

def eliminar_producto():
    if not ventas:
        print("No hay productos para eliminar.")
        return
    
    suma_columnas = []
    for j in range(len(productos)):
        suma_columna = 0
        for i in range(len(ventas)):
            suma_columna += ventas[i][j]
        suma_columnas.append(suma_columna)
    
    indice_columna_min = 0
    min_suma = suma_columnas[0]
    for j in range(1, len(productos)):
        if suma_columnas[j] < min_suma:
            min_suma = suma_columnas[j]
            indice_columna_min = j
    
    for fila in ventas:
        del fila[indice_columna_min]

    print(f"\nProducto eliminado correspondiente al año {años[indice_columna_min]}.")

def menu():
    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Cargar ventas de los productos por períodos")
        print("2. Mostrar matriz de ventas")
        print("3. Mostrar año de la venta máxima y producto correspondiente")
        print("4. Insertar nuevo período (fila)")
        print("5. Eliminar producto (columna) cuya suma sea la menor")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            cargar_ventas()
        elif opcion == "2":
            mostrar_datos()
        elif opcion == "3":
            encontrar_venta_maxima()
        elif opcion == "4":
            insertar_periodo()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Ingrese un número del 1 al 6.")

#PRINCIPAL
menu()
