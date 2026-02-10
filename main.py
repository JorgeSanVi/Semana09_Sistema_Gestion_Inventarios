# Archivo principal del sistema de gestión de inventarios
# Aquí se muestra el menú y se controla la interacción con el usuario

from modelos.producto import Producto
from servicios.inventario import Inventario


# Función para leer números enteros y validar la entrada
def leer_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Ingrese un número entero válido.")


# Función para leer números decimales y validar la entrada
def leer_flotante(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("No se permiten valores negativos.")
            else:
                return valor
        except ValueError:
            print("Ingrese un número válido.")


# Función principal que muestra el menú del sistema
def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DEL INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Listar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para añadir un producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = leer_entero("Cantidad: ")
            precio = leer_flotante("Precio: ")

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Opción para eliminar un producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Opción para actualizar un producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("1. Actualizar cantidad")
            print("2. Actualizar precio")
            print("3. Actualizar cantidad y precio")

            sub_op = input("Seleccione una opción: ")

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
            # Opción para buscar productos por nombre
            nombre = input("Ingrese el nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            # Opción para listar todos los productos
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Opción para salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida, intente nuevamente.")


# Punto de inicio del programa
if __name__ == "__main__":
    menu()
