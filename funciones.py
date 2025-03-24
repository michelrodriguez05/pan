import random

# Generar un código único para productos/pedidos
def generar_codigo(prefijo):
    return f"{prefijo}-{random.randint(1000, 9999)}"

# Validar si hay suficiente stock
def verificar_stock(stock_actual, cantidad):
    if cantidad <= 0:
        return False, "La cantidad debe ser mayor a 0."
    if stock_actual < cantidad:
        return False, f"Stock insuficiente. Disponible: {stock_actual}."
    return True, "Stock disponible."