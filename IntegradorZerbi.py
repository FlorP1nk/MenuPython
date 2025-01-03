# Importar el módulo
import sqlite3

# Crear base de datos
def crear_tabla():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT NOT NULL,
             descripcion TEXT,
             cantidad INTEGER NOT NULL,
             precio REAL NOT NULL,
             categoria TEXT
            )
         ''')
 
    conn.commit()
    conn.close()

crear_tabla()


# Registro de productos
def registrar_producto(nombre, descripcion, cantidad, precio, categoria):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    
    conn.commit()
    conn.close()


# Mostrar productos
def mostrar_productos():
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    for producto in productos:
        print(f'ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}')
    
    conn.commit()
    conn.close()

# Actualización de productos
def actualizar_producto(id_producto, cantidad_nueva):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE productos SET cantidad = ? WHERE id = ?
    ''', (cantidad_nueva, id_producto))
    
    conn.commit()
    conn.close()
    

# Eliminación de productos
def eliminar_producto(id_producto):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    
    conn.commit()
    conn.close()

# Búsqueda de productos
def buscar_producto_por_id(id_producto):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    producto = cursor.fetchone()
    
    if producto:
        print(f'ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}')
    else:
        print("Producto no encontrado.")
    
    conn.close()

# Reporte de bajo stock
def reporte_bajo_stock(limite):
    conn = sqlite3.connect('inventario.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM productos WHERE cantidad <= ?', (limite,))
    productos_bajo_stock = cursor.fetchall()
    
    if productos_bajo_stock:
        print("Productos con bajo stock:")
        for producto in productos_bajo_stock:
            print(f'ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}')
    else:
        print("No hay productos con bajo stock.")
    
    conn.close()

# Importación colorama
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Menú
def mostrar_menu():
    print(Fore.CYAN + "=== Menú de Inventario ===")
    print(Fore.GREEN + "1. Registrar producto")
    print(Fore.GREEN + "2. Mostrar productos")
    print(Fore.GREEN + "3. Actualizar producto")
    print(Fore.GREEN + "4. Eliminar producto")
    print(Fore.GREEN + "5. Buscar producto")
    print(Fore.GREEN + "6. Reporte de bajo stock")
    print(Fore.RED + "7. Salir")

# Interfaz de usuario    
def interfaz_usuario():
    while True:
        mostrar_menu()
        opcion = input(Fore.YELLOW + "Selecciona una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            registrar_producto(nombre, descripcion, cantidad, precio, categoria)
        
        elif opcion == "2":
            mostrar_productos()
        
        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad_nueva = int(input("Nueva cantidad: "))
            actualizar_producto(id_producto, cantidad_nueva)
        
        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
        
        elif opcion == "5":
            id_producto = int(input("ID del producto a buscar: "))
            buscar_producto_por_id(id_producto)
        
        elif opcion == "6":
            limite = int(input("Límite de stock bajo: "))
            reporte_bajo_stock(limite)
        
        elif opcion == "7":
            print(Fore.RED + "Saliendo...")
            break
        else:
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")

# Iniciar la interfaz
interfaz_usuario()

