def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encuentra el índice del menor elemento desde i hasta el final
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Intercambia el menor elemento con el actual
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ejemplo de uso
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = selection_sort(data)
print("Arreglo ordenado:", sorted_data)

#Bucle externo:
#Recorre el arreglo completo con n iteraciones.

#Bucle interno:
#Para cada posición  realiza n −i−1 comparaciones para encontrar el mínimo.


#El orden de magnitud es O(n^2) porque el algoritmo realiza un número cuadrático de comparaciones, lo que lo hace ineficiente
#para grandes conjuntos de datos.Es adecuado solo para conjuntos pequeños o cuando la simplicidad es preferible a la velocidad.