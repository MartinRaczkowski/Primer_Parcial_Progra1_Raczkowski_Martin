def cambiar_filas_por_columnas(matriz: list[list]) -> list[list]:
    """_summary_ Recibe una matriz e intercambia sus filas por sus columnas

    Args:
        matriz (list[list]): _description_

    Returns:
        list[list]: _description_
    """
    nueva_matriz = []
    columnas = len(matriz)
    for i in range(len(matriz[0])):
        fila = [0] * columnas
        nueva_matriz.append(fila)

    for i in range(len(nueva_matriz)):
        for j in range(len(matriz)):
            nueva_matriz[i][j] = matriz[j][i]

    return nueva_matriz

def validar_numero(minimo: int, maximo: int) -> int:
    """_summary_ Recibe un numero entero minimo y uno maximo, le solicita al usuario que ingrese un numero entero entre esos parametros y valida que sea correcto

    Args:
        minimo (int): _description_ 
        maximo (int): _description_ 

    Returns:
        int: _description_ Devuelve el numero ingresado por el usuario
    """
    numero = input(f'Ingrese un numero entre {minimo} y {maximo}: ')
    if not numero.isdigit() or not(minimo <= int(numero) <= maximo):
        return validar_numero(minimo, maximo)
    
    return int(numero)


