# Sistema de Gestión de Inventarios (Consola)
# Punto de inicio del programa

from modelos.producto import Producto
from servicios.inventario import Inventario


def leer_entero(mensaje):
    """Lee un número entero validando la entrada."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: no se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Error: ingresa un número entero válido.")


def leer_flotante(mensaje):
    """Lee un número decimal validando la entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: no se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Error: ingresa un número válido (ej: 2.50).")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Elige una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- Añadir producto ---")
            id_producto = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            print("\n--- Eliminar producto ---")
            id_producto = input("Ingresa el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            print("\n--- Actualizar producto ---")
            id_producto = input("Ingresa el ID del producto a actualizar: ").strip()

            print("¿Qué deseas actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            print("3. Cantidad y precio")

            sub_op = input("Elige una opción (1-3): ").strip()

            if sub_op == "1":
                nueva_cantidad = leer_entero("Nueva cantidad: ")
                inventario.actualizar_producto(id_producto, cantidad=nueva_cantidad)

            elif sub_op == "2":
                nuevo_precio = leer_flotante("Nuevo precio: ")
                inventario.actualizar_producto(id_producto, precio=nuevo_precio)

            elif sub_op == "3":
                nueva_cantidad = leer_entero("Nueva cantidad: ")
                nuevo_precio = leer_flotante("Nuevo precio: ")
                inventario.actualizar_producto(id_producto, cantidad=nueva_cantidad, precio=nuevo_precio)

            else:
                print("Opción inválida en actualización.")

        elif opcion == "4":
            print("\n--- Buscar producto ---")
            nombre = input("Ingresa el nombre o parte del nombre: ").strip()
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            print("\n--- Listar inventario ---")
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema... ¡Listo!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
