import data

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_PEDIDOS = "pedidos.json"

def buscar_producto_por_nombre():
    productos = data.cargar_datos(ARCHIVO_PRODUCTOS)
    nombre = input("Ingrese el nombre del producto: ").lower()

    resultados = [p for p in productos if nombre in p["nombre"].lower()]
    
    if resultados:
        for p in resultados:
            print(f"Código: {p['codigo']}, Nombre: {p['nombre']}, Stock: {p['stock']}")
    else:
        print("No se encontraron productos.")

def buscar_pedido_por_codigo():
    pedidos = data.cargar_datos(ARCHIVO_PEDIDOS)
    codigo = input("Ingrese el código del pedido: ")

    pedido = next((p for p in pedidos if p["codigo"] == codigo), None)

    if pedido:
        print(f"Código: {pedido['codigo']}, Producto: {pedido['producto']}, Cantidad: {pedido['cantidad']}")
    else:
        print("Pedido no encontrado.")
