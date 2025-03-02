# Matriz bidimensional (3x3)
matriz = [
    [7, 12, 13],
    [14, 45, 16],
    [17, 18, 8]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorrer filas
        for j in range(len(matriz[i])):  # Recorrer columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si lo encuentra
    return None  # Si no encuentra el valor

# Valor a buscar
valor_a_buscar = 13
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostrar resultado
if resultado:
    print(f"Valor {valor_a_buscar} encontrado en la posición {resultado}")
else:
    print(f"Valor {valor_a_buscar} no encontrado.")