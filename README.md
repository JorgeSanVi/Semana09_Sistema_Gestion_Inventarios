# Sistema de Gestión de Inventarios – Semana 09 y Semana 10

En estas semanas desarrollé y luego mejoré un sistema de gestión de inventarios usando **Python** y **Programación Orientada a Objetos (POO)**.  
El programa funciona en consola y me permite registrar productos de una tienda de forma sencilla.

---

## Semana 09: Versión inicial del inventario (POO)

En la Semana 09 realicé el sistema base, donde el programa permite:

- **Añadir** productos con: **ID, nombre, cantidad y precio**.
- **Eliminar** productos usando su **ID**.
- **Actualizar** la **cantidad** o el **precio** de un producto.
- **Buscar** productos por nombre (incluye coincidencias parciales).
- **Listar** todos los productos registrados.

**Organización del proyecto:**
- **modelos/**: contiene la clase `Producto`.
- **servicios/**: contiene la clase `Inventario` y la lógica principal.
- **main.py**: ejecuta el menú y permite interactuar con el sistema.

---

## Semana 10: Mejora con archivos y manejo de excepciones

En la Semana 10 mejoré el sistema para que la información **no se pierda al cerrar el programa**, usando archivos y controlando errores.

### 1) Guardado en archivo (`inventario.txt`)
- El inventario se guarda automáticamente en **`inventario.txt`**.
- Cada vez que **agrego, actualizo o elimino** un producto, el archivo se actualiza con los cambios.

### 2) Carga automática al iniciar
- Al ejecutar el programa, se leen los datos de **`inventario.txt`** y se reconstruye el inventario en memoria.

### 3) Manejo de excepciones
Para que el sistema sea más seguro y no se cierre por errores:
- **FileNotFoundError:** si el archivo no existe, el programa lo crea y continúa.
- **PermissionError:** si no hay permisos para leer o escribir, se muestra un mensaje y el programa evita fallar.
- Si hay líneas incorrectas o dañadas en el archivo, el programa las ignora y sigue cargando lo válido.

---

## Formato del archivo `inventario.txt`
Cada producto se guarda en una sola línea con este formato:

`id;nombre;cantidad;precio`

Ejemplo:

`1;arroz;10;48.0`

---

## Cómo ejecutar el programa
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:

`python main.py`

---

## Pruebas realizadas (Semana 10)
Para comprobar que el sistema funciona bien, realicé estas pruebas:

- Inicié el programa con `inventario.txt` vacío y verifiqué que carga sin errores.
- Agregué productos y confirmé que se guardan automáticamente en el archivo.
- Actualicé cantidad/precio y comprobé que el archivo se modifica correctamente.
- Eliminé productos y verifiqué que desaparecen del archivo.
- Probé ejecutar sin `inventario.txt` y comprobé que el sistema lo crea (manejo de `FileNotFoundError`).
- Probé con una línea mal escrita en el archivo y verifiqué que el programa no se cae y la ignora.

---

## Nota final
Durante el desarrollo validé las entradas del usuario para evitar errores comunes al ingresar datos.  
Además, utilicé un archivo **.gitignore** para mantener el repositorio ordenado y no subir archivos temporales de Python.