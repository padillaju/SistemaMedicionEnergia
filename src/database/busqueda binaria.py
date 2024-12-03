def busqueda_binaria_recursiva(lista, elemento, izquierda, derecha):
  """
  Realiza una búsqueda binaria recursiva en una lista ordenada.

  Args:
    lista: Una lista ordenada de elementos comparables.
    elemento: El elemento a buscar.
    izquierda: Índice inicial de la sublista.
    derecha: Índice final de la sublista.

  Returns:
    El índice del elemento si se encuentra, o -1 si no se encuentra.
  """

  if izquierda > derecha:
      return -1

  medio = (izquierda + derecha) // 2

  if lista[medio] == elemento:
      return medio
  elif lista[medio] < elemento:
      return busqueda_binaria_recursiva(lista, elemento, medio + 1, derecha)
  else:
      return busqueda_binaria_recursiva(lista, elemento, izquierda, medio - 1)

# Ejemplo de uso:
lista_ordenada = [2, 4, 6, 8, 10, 12]
elemento_a_buscar = 8

resultado = busqueda_binaria_recursiva(lista_ordenada, elemento_a_buscar, 0, len(lista_ordenada) - 1)

if resultado != -1:
  print("El elemento", elemento_a_buscar, "se encuentra en el índice", resultado)
else:
  print("El elemento", elemento_a_buscar, "no se encuentra en la lista")


