def cambiar_filas_por_columnas(matriz: list[list]) -> list[list]:

    nueva_matriz = []
    columnas = len(matriz)
    for i in range(len(matriz[0])):
        fila = [0] * columnas
        nueva_matriz.append(fila)

    for i in range(len(nueva_matriz)):
        for j in range(len(matriz)):
            nueva_matriz[i][j] = matriz[j][i]

    return nueva_matriz


