import time
import random

# Algoritmos de ordenación

# QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

# MergeSort
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    resultado.extend(izquierda)
    resultado.extend(derecha)
    return resultado

# Burbuja
def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Inserción
def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


# Función para medir el tiempo de ejecución
def medir_tiempos():
    tamanos = [100, 1000, 5000, 10000]
    resultados = {}

    for tamano in tamanos:
        lista = [random.randint(1, 10000) for _ in range(tamano)]
        print(f"\nLista de tamaño: {tamano}")

        # QuickSort
        inicio = time.time()
        quicksort(lista.copy())
        resultados[f"QuickSort {tamano}"] = time.time() - inicio

        # MergeSort
        inicio = time.time()
        mergesort(lista.copy())
        resultados[f"MergeSort {tamano}"] = time.time() - inicio

        # Burbuja
        inicio = time.time()
        burbuja(lista.copy())
        resultados[f"Burbuja {tamano}"] = time.time() - inicio

        # Inserción
        inicio = time.time()
        insercion(lista.copy())
        resultados[f"Inserción {tamano}"] = time.time() - inicio

    # Imprimir resultados
    print("\n--- Resultados ---")
    for key, value in resultados.items():
        print(f"{key}: {value:.4f} segundos")


# Llamar la función para medir y mostrar los tiempos
if __name__ == "__main__":
    medir_tiempos()
