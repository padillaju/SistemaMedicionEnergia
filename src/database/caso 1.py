# Datos de ejemplo para el catálogo (pueden cargarse desde un archivo)
catalogo = [
    {"id": 1, "nombre": "Laptop", "precio": 800, "categoria": "Electrónica"},
    {"id": 2, "nombre": "Teclado", "precio": 20, "categoria": "Accesorios"},
    {"id": 3, "nombre": "Monitor", "precio": 150, "categoria": "Electrónica"},
    {"id": 4, "nombre": "Silla", "precio": 85, "categoria": "Muebles"},
    {"id": 5, "nombre": "Mouse", "precio": 15, "categoria": "Accesorios"},
]

### a) Ordenar el catálogo por precio utilizando QuickSort
def quicksort(lista, clave):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x[clave] < pivote[clave]]
    iguales = [x for x in lista if x[clave] == pivote[clave]]
    mayores = [x for x in lista if x[clave] > pivote[clave]]
    return quicksort(menores, clave) + iguales + quicksort(mayores, clave)

### b) Buscar producto por identificador usando búsqueda binaria
def busqueda_binaria(lista, clave, valor):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][clave] == valor:
            return lista[medio]
        elif lista[medio][clave] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

### c) Buscar productos por categoría usando búsqueda secuencial
def busqueda_secuencial(lista, clave, valor):
    resultado = [producto for producto in lista if producto[clave] == valor]
    return resultado

### Programa principal
if __name__ == "__main__":
    print("Catálogo original:")
    for producto in catalogo:
        print(producto)

    # a) Ordenar por precio
    catalogo_ordenado = quicksort(catalogo, "precio")
    print("\nCatálogo ordenado por precio:")
    for producto in catalogo_ordenado:
        print(producto)

    # b) Buscar producto por identificador
    id_buscar = 3
    producto = busqueda_binaria(catalogo_ordenado, "id", id_buscar)
    if producto:
        print(f"\nProducto con ID {id_buscar}: {producto}")
    else:
        print(f"\nProducto con ID {id_buscar} no encontrado.")

    # c) Buscar productos por categoría
    categoria_buscar = "Electrónica"
    productos_en_categoria = busqueda_secuencial(catalogo, "categoria", categoria_buscar)
    print(f"\nProductos en la categoría '{categoria_buscar}':")
    for producto in productos_en_categoria:
        print(producto)
