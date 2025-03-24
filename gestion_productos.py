import data
import funciones

ARCHIVO_PRODUCTOS = "productos.json"

def menu_productos():
    while True:
        print("\n=== Gestión de Productos ===")
        print("1. Agregar producto")
        print("2. Editar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            editar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            listar_productos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

# 1. Agregar Producto
def agregar_producto():
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)
    codigos_existentes = {p["codigo"] for p in productos}
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría: ")
    descripcion = input("Ingrese la descripción: ")
    proveedor = input("Ingrese el proveedor: ")
    precio_compra = float(input("Ingrese el precio de compra: "))
    precio_venta = float(input("Ingrese el precio de venta: "))
    stock = int(input("Ingrese la cantidad en stock: "))


    if precio_compra <= 0 or precio_venta <= 0 or stock < 0:
        print("Error: Precio y stock deben ser positivos.")
        return
    codigo = funciones.generar_codigo("PROD").lower()
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "descripcion": descripcion,
        "proveedor": proveedor,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta,
        "stock": stock
    }

    productos.append(nuevo_producto)
    data.guardar_datos(ARCHIVO_PRODUCTOS, productos)
    print(f"Producto {nombre} agregado con éxito.")

# 2. Editar Producto
def editar_producto():
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)
    listar_productos()

    codigo = input("Ingrese el código del producto a editar: ")
    producto = next((p for p in productos if p["codigo"] == codigo), None)

    if not producto:
        print("Producto no encontrado.")
        return

    print("\nDeje en blanco si no desea cambiar un campo.")
    nuevo_nombre = input(f"Nuevo nombre ({producto['nombre']}): ") or producto["nombre"]
    nueva_categoria = input(f"Nueva categoría ({producto['categoria']}): ") or producto["categoria"]
    nueva_descripcion = input(f"Nueva descripción ({producto['descripcion']}): ") or producto["descripcion"]
    nuevo_proveedor = input(f"Nuevo proveedor ({producto['proveedor']}): ") or producto["proveedor"]
    nuevo_precio_compra = input(f"Nuevo precio de compra ({producto['precio_compra']}): ") or producto["precio_compra"]
    nuevo_precio_venta = input(f"Nuevo precio de venta ({producto['precio_venta']}): ") or producto["precio_venta"]
    nuevo_stock = input(f"Nuevo stock ({producto['stock']}): ") or producto["stock"]

    producto.update({
        "nombre": nuevo_nombre,
        "categoria": nueva_categoria,
        "descripcion": nueva_descripcion,
        "proveedor": nuevo_proveedor,
        "precio_compra": float(nuevo_precio_compra),
        "precio_venta": float(nuevo_precio_venta),
        "stock": int(nuevo_stock)
    })

    data.guardar_datos(ARCHIVO_PRODUCTOS, productos)
    print("Producto actualizado con éxito.")

# 3. Eliminar Producto
def eliminar_producto():
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)
    listar_productos()

    codigo = input("Ingrese el código del producto a eliminar: ")
    productos_filtrados = [p for p in productos if p["codigo"] != codigo]

    if len(productos) == len(productos_filtrados):
        print("Producto no encontrado.")
    else:
        data.guardar_datos(ARCHIVO_PRODUCTOS, productos_filtrados)
        print("Producto eliminado con éxito.")

# 4. Listar Productos
def listar_productos():
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)
    
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\n=== Lista de Productos ===")
    for p in productos:
        print(f"Código: {p['codigo']} | Nombre: {p['nombre']} | Categoría: {p['categoria']} | "
              f"Descripción: {p['descripcion']} | Proveedor: {p['proveedor']} | "
              f"Precio de Compra: {p['precio_compra']} | Precio de Venta: {p['precio_venta']} | "
              f"Stock: {p['stock']}")
