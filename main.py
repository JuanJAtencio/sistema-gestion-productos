# ===============================
# Sistema de Gestión de Productos
# ===============================

from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Lista que simula la base de datos
productos = []
id_actual = 1  # ID autoincremental


# ===============================
# FUNCIONES CRUD
# ===============================

def registrar_producto():
    """Registra un nuevo producto"""
    global id_actual

    print(Fore.CYAN + "\n--- Registrar Producto ---")

    nombre = input("Nombre: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "id": id_actual,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)
    print(Fore.GREEN + "Producto registrado con éxito.")

    id_actual += 1


def mostrar_productos():
    """Muestra todos los productos"""
    print(Fore.CYAN + "\n--- Lista de Productos ---")

    if not productos:
        print(Fore.YELLOW + "No hay productos registrados.")
        return

    for p in productos:
        print(
            f"ID: {p['id']} | "
            f"Nombre: {p['nombre']} | "
            f"Categoría: {p['categoria']} | "
            f"Precio: ${p['precio']} | "
            f"Cantidad: {p['cantidad']}"
        )


def buscar_producto_por_id():
    """Busca un producto por ID"""
    print(Fore.CYAN + "\n--- Buscar Producto ---")

    id_buscar = int(input("Ingrese ID del producto: "))

    for p in productos:
        if p["id"] == id_buscar:
            print(Fore.GREEN + "Producto encontrado:")
            print(p)
            return

    print(Fore.RED + "Producto no encontrado.")


def actualizar_producto():
    """Actualiza un producto por ID"""
    print(Fore.CYAN + "\n--- Actualizar Producto ---")

    id_actualizar = int(input("Ingrese ID del producto: "))

    for p in productos:
        if p["id"] == id_actualizar:
            p["nombre"] = input("Nuevo nombre: ")
            p["categoria"] = input("Nueva categoría: ")
            p["precio"] = float(input("Nuevo precio: "))
            p["cantidad"] = int(input("Nueva cantidad: "))

            print(Fore.GREEN + "Producto actualizado correctamente.")
            return

    print(Fore.RED + "Producto no encontrado.")


def eliminar_producto():
    """Elimina un producto por ID"""
    print(Fore.CYAN + "\n--- Eliminar Producto ---")

    id_eliminar = int(input("Ingrese ID del producto: "))

    for p in productos:
        if p["id"] == id_eliminar:
            productos.remove(p)
            print(Fore.GREEN + "Producto eliminado.")
            return

    print(Fore.RED + "Producto no encontrado.")


def reporte_stock_bajo():
    """Muestra productos con stock bajo"""
    print(Fore.CYAN + "\n--- Reporte de Stock Bajo ---")

    limite = int(input("Ingrese el límite de cantidad: "))

    encontrados = False

    for p in productos:
        if p["cantidad"] <= limite:
            print(
                f"ID: {p['id']} | "
                f"Nombre: {p['nombre']} | "
                f"Cantidad: {p['cantidad']}"
            )
            encontrados = True

    if not encontrados:
        print(Fore.YELLOW + "No hay productos con stock bajo.")


# ===============================
# MENÚ PRINCIPAL
# ===============================

def mostrar_menu():
    """Muestra el menú principal"""
    print(Fore.BLUE + "\n===== MENÚ PRINCIPAL =====")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por ID")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Reporte de stock bajo")
    print("0. Salir")


def main():
    """Función principal"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto_por_id()
        elif opcion == "4":
            actualizar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_stock_bajo()
        elif opcion == "0":
            print(Fore.MAGENTA + "Saliendo del sistema...")
            break
        else:
            print(Fore.RED + "Opción inválida.")


# ===============================
# EJECUCIÓN
# ===============================

if __name__ == "__main__":
    main()
