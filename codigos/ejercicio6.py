def dar_bienvenida():
    print("Bienvenido al concurso de pesca!")

def cargar_listas(participantes, peces_capturados):
    n = int(input("Ingrese la cantidad de participantes (entre 10 y 50): "))
    while n < 10 or n > 50:
        print("Cantidad inválida. Debe ser entre 10 y 50.")
        n = int(input("Ingrese la cantidad de participantes (entre 10 y 50): "))

    for i in range(n):
        nombre = input(f"Ingrese el nombre del participante {i+1}: ")
        peces = int(input(f"Ingrese la cantidad de peces capturados por {nombre}: "))
        while peces < 0:
            print("La cantidad de peces capturados debe ser mayor o igual a 0.")
            peces = int(input(f"Ingrese la cantidad de peces capturados por {nombre}: "))

        participantes.append(nombre)
        peces_capturados.append(peces)

def mostrar_promedio(peces_capturados):
    if not peces_capturados:
        print("No hay datos para calcular el promedio.")
    else:
        promedio = sum(peces_capturados) / len(peces_capturados)
        print(f"El promedio de peces capturados es: {promedio:.2f}")

def mostrar_ganador(participantes, peces_capturados):
    if not peces_capturados:
        print("No hay participantes registrados.")
        return

    max_peces = max(peces_capturados)
    ganadores = [participantes[i] for i in range(len(participantes)) if peces_capturados[i] == max_peces]

    print(f"La mayor cantidad de peces capturados es: {max_peces}")
    print("Los ganadores son:")
    for ganador in ganadores:
        print(ganador)

def disminuir_peces(participantes, peces_capturados):
    if not peces_capturados:
        print("No hay participantes registrados.")
        return

    z = int(input("Ingrese la posición del participante a disminuir (1 - n): ")) - 1
    while z < 0 or z >= len(participantes):
        print(f"Posición inválida. Debe ser entre 1 y {len(participantes)}.")
        z = int(input("Ingrese la posición del participante a disminuir (1 - n): ")) - 1

    x = int(input(f"Ingrese la cantidad de peces a disminuir a {participantes[z]}: "))
    while x > peces_capturados[z]:
        print(f"No se puede disminuir más peces de los capturados ({peces_capturados[z]}).")
        x = int(input(f"Ingrese la cantidad de peces a disminuir a {participantes[z]}: "))

    peces_capturados[z] -= x
    print(f"Se han disminuido {x} peces a {participantes[z]}.")

def despedirse():
    print("Gracias por participar en el concurso de pesca. ¡Hasta luego!")

def menu():
    participantes = []
    peces_capturados = []

    while True:
        print("\nMENU:")
        print("1. Dar la bienvenida al concurso de pesca")
        print("2. Cargar listas de participantes y peces capturados")
        print("3. Mostrar el promedio de peces capturados")
        print("4. Mostrar el ganador (puede haber empates)")
        print("5. Disminuir peces capturados de un participante")
        print("6. Despedirse y salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            dar_bienvenida()
        elif opcion == "2":
            cargar_listas(participantes, peces_capturados)
        elif opcion == "3":
            mostrar_promedio(peces_capturados)
        elif opcion == "4":
            mostrar_ganador(participantes, peces_capturados)
        elif opcion == "5":
            disminuir_peces(participantes, peces_capturados)
        elif opcion == "6":
            despedirse()
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 6.")

# Programa principal: ejecutar el menú
menu()
