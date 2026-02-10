# Clase Inventario
# Esta clase se encarga de gestionar todos los productos del sistema.
# Utiliza una lista como estructura principal de almacenamiento.

from modelos.producto import Producto


class Inventario:
    def __init__(self):
        # Lista donde se almacenan los productos del inventario
        self.productos = []

    # Método para agregar un nuevo producto
    # Se valida que el ID no esté repetido
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Método para eliminar un producto usando su ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    # Método para actualizar la cantidad o el precio de un producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    # Método para buscar productos por nombre
    # Permite coincidencias parciales
    def buscar_producto(self, nombre):
        encontrado = False
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    # Método para mostrar todos los productos del inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)
