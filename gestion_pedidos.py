import data
import funciones

ARCHIVO_PEDIDOS = "pedidos.json"
ARCHIVO_PRODUCTOS = "productos.json"

def menu_pedidos():
    while True:
        print("\n=== Gestión de Pedidos ===")
        print("1. Crear pedido")
        print("2. Ver pedidos")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def crear_pedido():
    pedidos = data.cargar_datos(ARCHIVO_PEDIDOS)
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)

    print("Productos disponibles:")
    for p in productos:
        print(f"{p['codigo']} - {p['nombre']} (Stock: {p['stock']})")

    codigo_producto = input("Ingrese el código del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))

    producto = next((p for p in productos if p["codigo"] == codigo_producto), None)

    if not producto:
        print("Producto no encontrado.")
        return
    
    if not funciones.verificar_stock(producto["stock"], cantidad):
        print("Stock insuficiente.")
        return

    codigo_pedido = funciones.generar_codigo("PED")
    pedido = {
        "codigo": codigo_pedido,
        "producto": codigo_producto,
        "cantidad": cantidad
    }

    pedidos.append(pedido)
    data.guardar_datos(ARCHIVO_PEDIDOS, pedidos)

    # Reducir stock
    producto["stock"] -= cantidad
    data.guardar_datos(ARCHIVO_PRODUCTOS, productos)

    print(f"Pedido {codigo_pedido} registrado con éxito.")

def ver_pedidos():
    pedidos = data.cargar_datos(ARCHIVO_PEDIDOS)
    for p in pedidos:
        print(f"Código: {p['codigo']}, Producto: {p['producto']}, Cantidad: {p['cantidad']}")
