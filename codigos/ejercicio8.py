# Función para validar que las notas estén en el intervalo [0, 100]
def validar_nota(nota):
    if nota < 0 or nota > 100:
        return False
    return True

# Función para validar que el legajo no esté repetido
def validar_legajo(legajo, lista_legajos):
    if legajo in lista_legajos:
        return False
    return True

def cargar_registros(nombre, legajo, nota, lista_nombre, lista_legajo, lista_nota):
    while True:
        nombre.append(input("Ingrese el nombre del estudiante (o 'fin' para terminar): "))
        if nombre[-1].lower() == 'fin':
            nombre.pop()  # Eliminar el 'fin' ingresado
            break
        
        leg = int(input("Ingrese el legajo del estudiante: "))
        while not validar_legajo(leg, lista_legajo):
            print("¡Error! El legajo ingresado ya existe.")
            leg = int(input("Ingrese un legajo único para el estudiante: "))
        legajo.append(leg)
        lista_legajo.append(leg)
        
        nt = float(input("Ingrese la nota del estudiante: "))
        while not validar_nota(nt):
            print("¡Error! La nota debe estar en el rango de 0 a 100.")
            nt = float(input("Ingrese la nota del estudiante: "))
        nota.append(nt)
        lista_nota.append(nt)

        print("Estudiante registrado correctamente.")

def mostrar_registros(nombre, legajo, nota):
    if not nombre:
        print("No hay registros para mostrar.")
    else:
        print("Listado de registros:")
        for i in range(len(nombre)):
            print(f"Nombre: {nombre[i]}, Legajo: {legajo[i]}, Nota: {nota[i]}")

def mostrar_notas_superiores(nombre, legajo, nota):
    if not nombre:
        print("No hay registros para mostrar.")
    else:
        promedio = sum(nota) / len(nota)
        print(f"Notas superiores al promedio ({promedio}):")
        registros_superiores = sorted(zip(nombre, legajo, nota), key=lambda x: x[2], reverse=True)
        for nombre, legajo, nota in registros_superiores:
            if nota > promedio:
                print(f"Nombre: {nombre}, Legajo: {legajo}, Nota: {nota}")

def nota_maxima_minima(nombre, legajo, nota):
    if not nombre:
        print("No hay registros para mostrar.")
    else:
        max_nota = max(nota)
        min_nota = min(nota)
        cantidad_maximas = nota.count(max_nota)
        cantidad_minimas = nota.count(min_nota)
        
        print(f"Nota máxima: {max_nota}, cantidad de estudiantes que la obtuvieron: {cantidad_maximas}")
        print(f"Nota mínima: {min_nota}, cantidad de estudiantes que la obtuvieron: {cantidad_minimas}")

def agregar_registro(nombre, legajo, nota):
    nombre.append(input("Ingrese el nombre del estudiante: "))
    
    leg = int(input("Ingrese el legajo del estudiante: "))
    while not validar_legajo(leg, legajo):
        print("¡Error! El legajo ingresado ya existe.")
        leg = int(input("Ingrese un legajo único para el estudiante: "))
    legajo.append(leg)
    
    nt = float(input("Ingrese la nota del estudiante: "))
    while not validar_nota(nt):
        print("¡Error! La nota debe estar en el rango de 0 a 100.")
        nt = float(input("Ingrese la nota del estudiante: "))
    nota.append(nt)

    print("Estudiante agregado correctamente.")

def agregar_nueva_nota(nota):
    nueva_nota = float(input("Ingrese la nueva nota para todos los estudiantes: "))
    while not validar_nota(nueva_nota):
        print("¡Error! La nota debe estar en el rango de 0 a 100.")
        nueva_nota = float(input("Ingrese la nueva nota para todos los estudiantes: "))
    
    nota.extend([nueva_nota] * len(nota))
    print("Nueva nota agregada correctamente.")

def modificar_registro(legajo, nombre, nota):
    legajo_mod = int(input("Ingrese el legajo del estudiante a modificar: "))
    if legajo_mod in legajo:
        indice = legajo.index(legajo_mod)
        print(f"Estudiante encontrado: {nombre[indice]}, Nota actual: {nota[indice]}")
        
        nueva_nota = float(input("Ingrese la nueva nota para el estudiante: "))
        while not validar_nota(nueva_nota):
            print("¡Error! La nota debe estar en el rango de 0 a 100.")
            nueva_nota = float(input("Ingrese la nueva nota para el estudiante: "))
        
        nota[indice] = nueva_nota
        print("Nota modificada correctamente.")
    else:
        print("No se encontró ningún estudiante con ese legajo.")

def eliminar_registro(nombre, legajo, nota):
    legajo_elim = int(input("Ingrese el legajo del estudiante a eliminar: "))
    if legajo_elim in legajo:
        indice = legajo.index(legajo_elim)
        print(f"Estudiante eliminado: {nombre[indice]}, Legajo: {legajo[indice]}, Nota: {nota[indice]}")
        
        nombre.pop(indice)
        legajo.pop(indice)
        nota.pop(indice)
        
        print("Estudiante eliminado correctamente.")
    else:
        print("No se encontró ningún estudiante con ese legajo.")

# Menú principal
nombre = []
legajo = []
nota = []

while True:
    print("\nMENU DE OPCIONES:")
    print("a. Cargar registros de estudiantes")
    print("b. Mostrar registros de estudiantes")
    print("c. Mostrar registros cuyas notas superan al promedio")
    print("d. Mostrar nota máxima y mínima")
    print("e. Agregar un nuevo registro")
    print("f. Agregar una nueva nota para todos los estudiantes")
    print("g. Modificar un registro")
    print("h. Eliminar un registro")
    print("i. Salir")

    opcion = input("Ingrese la opción deseada (a-i): ").lower()

    if opcion == "a":
        cargar_registros(nombre, legajo, nota)
    elif opcion == "b":
        mostrar_registros(nombre, legajo, nota)
    elif opcion == "c":
        mostrar_notas_superiores(nombre, legajo, nota)
    elif opcion == "d":
        nota_maxima_minima(nombre, legajo, nota)
    elif opcion == "e":
        agregar_registro(nombre, legajo, nota)
    elif opcion == "f":
        agregar_nueva_nota(nota)
    elif opcion == "g":
        modificar_registro(legajo, nombre, nota)
    elif opcion == "h":
        eliminar_registro(nombre, legajo, nota)
    elif opcion == "i":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida (a-i).")
