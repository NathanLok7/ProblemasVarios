
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento actual a insertar en la sublista ordenada
        j = i - 1  # Índice del último elemento de la sublista ordenada
        
        # Mover elementos de la sublista ordenada que son mayores que key
        # a la derecha para hacer espacio para la inserción
        while j >= 0 and arr[j] > key:
            print("Lista original:", lista)

            arr[j + 1] = arr[j]
            j -= 1
        
        # Insertar el elemento en su posición correcta
        arr[j + 1] = key

# Ejemplo de uso
lista = [12, 11, 13, 5, 6]
print("Lista original:", lista)

print(), print()
insertion_sort(lista)
print("Lista ordenada:", lista)


