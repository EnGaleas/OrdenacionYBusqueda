# Matriz bidimensional (3x3)
matriz = [
    [7, 12, 13],
    [14, 45, 16],
    [17, 18, 8]
]

# Función para ordenar la fila (por ejemplo la fila 1)
def ordenar_fila(matriz, fila_index):
    # Ordenar fila en orden ascendente
    matriz[fila_index].sort()

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1
ordenar_fila(matriz, 1)

# Mostrar la matriz después de ordenar
print("\nMatriz después de ordenar la fila 1:")
for fila in matriz:
    print(fila)