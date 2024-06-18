def registrar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    # Validación de código único
    while codigo in productos:
        print("¡Error! El código ingresado ya existe.")
        codigo = input("Ingrese un código único para el producto: ")

    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while precio < 0:
        print("¡Error! El precio no puede ser negativo.")
        precio = float(input("Ingrese el precio del producto: "))

    stock = int(input("Ingrese el stock inicial del producto: "))
    while stock < 0:
        print("¡Error! El stock no puede ser negativo.")
        stock = int(input("Ingrese el stock inicial del producto: "))

    productos[codigo] = {'descripcion': descripcion, 'precio': precio, 'stock': stock}
    print("Producto registrado correctamente.")

def mostrar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
    else:
        print("Listado de productos:")
        for codigo, producto in productos.items():
            print(f"Código: {codigo}, Descripción: {producto['descripcion']}, Precio: ${producto['precio']:.2f}, Stock: {producto['stock']}")

def productos_con_stock_menor(productos):
    valor_limite = int(input("Ingrese el valor límite de stock: "))
    print(f"Productos con stock menor a {valor_limite}:")
    encontrado = False
    for codigo, producto in productos.items():
        if producto['stock'] < valor_limite:
            encontrado = True
            print(f"Código: {codigo}, Descripción: {producto['descripcion']}, Precio: ${producto['precio']:.2f}, Stock: {producto['stock']}")
    if not encontrado:
        print("No se encontraron productos con stock menor al valor ingresado.")

def incrementar_stock(productos):
    codigo = input("Ingrese el código del producto a incrementar el stock: ")
    if codigo in productos:
        cantidad = int(input("Ingrese la cantidad a incrementar: "))
        while cantidad <= 0:
            print("La cantidad a incrementar debe ser mayor que cero.")
            cantidad = int(input("Ingrese la cantidad a incrementar: "))
        
        productos[codigo]['stock'] += cantidad
        print(f"Stock de {productos[codigo]['descripcion']} incrementado en {cantidad}. Stock actual: {productos[codigo]['stock']}")
    else:
        print("¡Error! Producto no encontrado.")

def producto_menor_precio(productos):
    if not productos:
        print("No hay productos registrados.")
    else:
        menor_precio = float('inf')
        producto_menor = None
        for codigo, producto in productos.items():
            if producto['precio'] < menor_precio:
                menor_precio = producto['precio']
                producto_menor = producto

        if producto_menor:
            print(f"Producto de menor precio:")
            print(f"Código: {codigo}, Descripción: {producto_menor['descripcion']}, Precio: ${producto_menor['precio']:.2f}, Stock: {producto_menor['stock']}")
        else:
            print("No hay productos registrados.")

def buscar_precio_mas_alto(productos):
    if not productos:
        print("No hay productos registrados.")
    else:
        max_precio = -float('inf')
        productos_max = []
        for codigo, producto in productos.items():
            if producto['precio'] > max_precio:
                max_precio = producto['precio']
                productos_max = [(codigo, producto)]
            elif producto['precio'] == max_precio:
                productos_max.append((codigo, producto))

        print(f"Precio más alto encontrado: ${max_precio:.2f}")
        print("Productos con el precio más alto:")
        for codigo, producto in productos_max:
            print(f"Código: {codigo}, Descripción: {producto['descripcion']}, Precio: ${producto['precio']:.2f}, Stock: {producto['stock']}")

def menu():
    productos = {}

    while True:
        print("\nMENU DE OPCIONES:")
        print("1. Registrar producto")
        print("2. Mostrar listado de productos")
        print("3. Mostrar productos con stock menor a un valor dado")
        print("4. Incrementar stock de un producto")
        print("5. Mostrar producto de menor precio")
        print("6. Buscar precio más alto y listar productos")
        print("7. Salir del programa")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            productos_con_stock_menor(productos)
        elif opcion == "4":
            incrementar_stock(productos)
        elif opcion == "5":
            producto_menor_precio(productos)
        elif opcion == "6":
            buscar_precio_mas_alto(productos)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Ingrese un número del 1 al 7.")

# Ejecutar el programa
menu()
