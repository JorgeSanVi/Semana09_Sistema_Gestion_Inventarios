# modelos/producto.py
# ------------------------------------------------------------
# Clase Producto:
# Representa un producto dentro del inventario.
# Guarda: id, nombre, cantidad y precio.
# Incluye getters/setters y una forma bonita de mostrar el producto.
# ------------------------------------------------------------

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados (encapsulación)
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ===== Getters (obtener valores) =====
    def get_id_producto(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ===== Setters (modificar valores) =====
    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Mostrar el producto de forma clara en consola
    def __str__(self):
        return (
            f"ID: {self.__id_producto} | "
            f"Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__precio}"
        )
        