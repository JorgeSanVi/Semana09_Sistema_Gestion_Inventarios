from modelos.producto import Producto

class Inventario:
    def __init__(self, ruta_archivo="inventario.txt"):
        # Lista donde se guardan los productos en memoria
        self.productos = []
        # Ruta del archivo donde se almacena el inventario
        self.ruta_archivo = ruta_archivo
        # Cargar datos del archivo al iniciar
        self.cargar_desde_archivo()

    # -------------------- MÉTODOS DE ARCHIVO --------------------

    def cargar_desde_archivo(self):
        """
        Lee inventario.txt y reconstruye la lista de productos.
        Formato por línea: id;nombre;cantidad;precio
        Si el archivo no existe, se crea vacío.
        """
        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue

                    try:
                        partes = linea.split(";")
                        if len(partes) != 4:
                            print("⚠️ Línea inválida, se ignoró:", linea)
                            continue

                        id_producto = partes[0]
                        nombre = partes[1]
                        cantidad = int(partes[2])
                        precio = float(partes[3])

                        self.productos.append(Producto(id_producto, nombre, cantidad, precio))

                    except ValueError:
                        print("⚠️ Línea corrupta (números inválidos), se ignoró:", linea)

            print("✅ Inventario cargado desde inventario.txt")

        except FileNotFoundError:
            # Si el archivo no existe, lo creamos vacío y seguimos
            try:
                with open(self.ruta_archivo, "a", encoding="utf-8"):
                    pass
                print("⚠️ No existía inventario.txt, se creó uno nuevo.")
            except PermissionError:
                print("❌ No se pudo crear inventario.txt: permisos denegados.")

        except PermissionError:
            print("❌ No se pudo leer inventario.txt: permisos denegados.")

    def guardar_en_archivo(self):
        """
        Guarda todo el inventario en inventario.txt (reescribe el archivo).
        Retorna True si guardó, False si no se pudo.
        """
        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
                for p in self.productos:
                    linea = f"{p.get_id_producto()};{p.get_nombre()};{p.get_cantidad()};{p.get_precio()}\n"
                    archivo.write(linea)
            return True

        except PermissionError:
            print("❌ No se pudo guardar en inventario.txt: permisos denegados.")
            return False

    # -------------------- MÉTODOS DEL INVENTARIO --------------------

    def agregar_producto(self, producto):
        # Validar ID repetido
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: El ID del producto ya existe.")
                return

        self.productos.append(producto)

        if self.guardar_en_archivo():
            print("✅ Producto agregado y guardado en inventario.txt")
        else:
            print("⚠️ Producto agregado, pero NO se pudo guardar en el archivo.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)

                if self.guardar_en_archivo():
                    print("✅ Producto eliminado y cambios guardados.")
                else:
                    print("⚠️ Producto eliminado, pero NO se pudo guardar en el archivo.")
                return

        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)

                if self.guardar_en_archivo():
                    print("✅ Producto actualizado y cambios guardados.")
                else:
                    print("⚠️ Producto actualizado, pero NO se pudo guardar en el archivo.")
                return

        print("Error: Producto no encontrado.")

    def buscar_productos(self, nombre):
        encontrado = False
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                print(p)
                encontrado = True

        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)