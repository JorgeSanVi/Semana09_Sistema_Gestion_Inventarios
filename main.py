# main.py
# ------------------------------------------------------------
# Menú principal del sistema de inventario (consola).
# - Pide datos al usuario.
# - Llama a los métodos del Inventario.
# - El Inventario se carga automáticamente desde inventario.txt al iniciar.
# ------------------------------------------------------------

from modelos.producto import Producto
from servicios.inventario import Inventario


def leer_entero(mensaje):
    """
    Lee un entero desde teclado, evitando errores si el usuario escribe letras.
    También evita negativos (porque cantidad no debe ser negativa).
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Ingresa un número entero válido.")


def leer_flotante(mensaje):
    """
    Lee un número decimal (float) desde teclado.
    Evita errores si el usuario escribe algo que no es número.
    También evita negativos (precio no debe ser negativo).
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Ingresa un número válido.")


def menu():
    # Al crear Inventario, se carga el archivo inventario.txt automáticamente
    inventario = Inventario("inventario.txt")

    while True:
        print("\n--- MENÚ DEL INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Crear producto con los datos ingresados
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar producto por ID
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar cantidad o precio (o ambos)
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("1. Actualizar cantidad")
            print("2. Actualizar precio")
            print("3. Actualizar cantidad y precio")
            sub_op = input("Selecciona una opción: ")

            if sub_op == "1":
                cantidad = leer_entero("Nueva cantidad: ")
                inventario.actualizar_producto(id_producto, cantidad=cantidad)

            elif sub_op == "2":
                precio = leer_flotante("Nuevo precio: ")
                inventario.actualizar_producto(id_producto, precio=precio)

            elif sub_op == "3":
                cantidad = leer_entero("Nueva cantidad: ")
                precio = leer_flotante("Nuevo precio: ")
                inventario.actualizar_producto(id_producto, cantidad=cantidad, precio=precio)

            else:
                print("Opción inválida.")

        elif opcion == "4":
            # Buscar por nombre (coincidencia parcial)
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == "5":
            # Listar todos los productos
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Salir
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intenta nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()