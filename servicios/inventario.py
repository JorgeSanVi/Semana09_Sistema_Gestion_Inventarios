# Clase Inventario
# Gestiona la lista de productos

from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # Lista principal de almacenamiento

    # Añadir producto (validar ID único)
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado correctamente.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar cantidad o precio por ID
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

    # Buscar productos por nombre (coincidencia parcial)
    def buscar_producto(self, nombre):
        encontrados = False
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrados = True
        if not encontrados:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_inventario(self):
        if not self.produ
