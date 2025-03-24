import gestion_productos
import gestion_pedidos

def mostrar_menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Gestión de productos")
        print("2. Gestión de pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestion_productos.menu_productos()
        elif opcion == "2":
            gestion_pedidos.menu_pedidos()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
