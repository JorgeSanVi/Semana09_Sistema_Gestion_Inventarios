# Clase Producto
# Esta clase representa a un producto dentro del inventario.
# Aquí se definen sus datos principales y los métodos para acceder y modificarlos.

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor de la clase Producto
        # Inicializa los atributos del producto
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ===== Getters =====
    # Permiten obtener los valores de los atributos

    def get_id_producto(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # ===== Setters =====
    # Permiten modificar los valores de los atributos

    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Método para mostrar la información del producto de forma legible
    def __str__(self):
        return (
            f"ID: {self.__id_producto} | "
            f"Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__precio}"
        )
