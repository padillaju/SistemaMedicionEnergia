# Función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i, num in enumerate(lista):
        if num == objetivo:
            return f"Encontrado en la posición {i}"
    return "No encontrado"

# Función de búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return f"Encontrado en la posición {medio}"
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return "No encontrado"

# Programa principal
lista_desordenada = [7, 2, 9, 3, 8, 1, 5]
lista_ordenada = sorted(lista_desordenada)  # Ordenamos la lista para la búsqueda binaria

numero_a_buscar = int(input("Ingresa el número a buscar: "))

# Búsqueda lineal
print("\n--- Búsqueda Lineal ---")
print(busqueda_lineal(lista_desordenada, numero_a_buscar))

# Búsqueda binaria
print("\n--- Búsqueda Binaria ---")
print(busqueda_binaria(lista_ordenada, numero_a_buscar))
