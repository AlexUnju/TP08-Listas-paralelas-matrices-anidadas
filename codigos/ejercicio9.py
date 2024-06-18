# Lista de pruebas de medicinas con ratones
# [tolerancia_raton1, tolerancia_raton2]
prueba1 = [0.8, 0.9]
prueba2 = [0.7, 0.6]
prueba3 = [0.5, 0.4]

# Lista de todas las pruebas
pruebas = [prueba1, prueba2, prueba3]

def ingresar_datos():
    pruebas = []
    while True:
        tolerancias = []
        for i in range(2):  # Se aplican a pares de ratones
            tolerancia = float(input(f"Ingrese la tolerancia del ratón {i+1}: "))
            while tolerancia < 0 or tolerancia > 1:
                print("La tolerancia debe estar en el rango [0, 1].")
                tolerancia = float(input(f"Ingrese la tolerancia del ratón {i+1}: "))
            tolerancias.append(tolerancia)
        pruebas.append(tolerancias)
        
        continuar = input("¿Desea ingresar otra prueba (s/n)? ")
        if continuar.lower() != 's':
            break
    
    return pruebas

def calcular_promedio(pruebas):
    promedios = []
    for prueba in pruebas:
        promedio = sum(prueba) / len(prueba)
        promedios.append(promedio)
    return promedios

def encontrar_mayor_promedio(promedios):
    indice_max = promedios.index(max(promedios))
    return indice_max, promedios[indice_max]

def encontrar_menor_suma(pruebas):
    sumas = [sum(prueba) for prueba in pruebas]
    indice_min = sumas.index(min(sumas))
    return indice_min, min(sumas)

def menu():
    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Ingresar datos de pruebas")
        print("2. Mostrar medicina con mayor promedio de tolerancia")
        print("3. Mostrar prueba con menor suma de tolerancia")
        print("4. Salir del programa")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            pruebas = ingresar_datos()
        elif opcion == "2":
            promedios = calcular_promedio(pruebas)
            indice_max_promedio, max_promedio = encontrar_mayor_promedio(promedios)
            print(f"La medicina con el promedio más alto de tolerancia es la prueba {indice_max_promedio + 1}, con promedio {max_promedio:.2f}")
        elif opcion == "3":
            indice_min_suma, min_suma = encontrar_menor_suma(pruebas)
            print(f"La prueba con la menor suma de tolerancia es la prueba {indice_min_suma + 1}, con suma {min_suma:.2f}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 4.")

# Ejecutar el programa
menu()
