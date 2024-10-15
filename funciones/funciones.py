from funciones.auxiliares import encontrar_minimo
#1 - Obtener existencias: para ello deberá crear una función que cargue la existencia de cada vehículo en todos los garajes y mostrarlos.

def obtener_existencias(matriz: list[list]) -> list[list]:

    #las existencias ya estan cargadas en la matriz
    for i in range(len(matriz)):
        print(f'La existencia del modelo {matriz[i][1]} en el garaje {i + 1} es de: {matriz[i][2]} unidades')

#2 - Calcular por cada garaje la cantidad total de unidades almacenadas entre todos los vehículos de la concesionaria.

def mostrar_total_de_unidades_almacenadas(matriz: list[list]):

    total = 0
    for i in range(len(matriz)):
        total += matriz[i][2]

    print(f'El total de unidades almacenadas en la concesionaria es de {total} vehiculos')

#3 - Datos completos del garaje que almacena menos unidades de vehículos.

def datos_garaje_con_menor_unidades(matriz: list[list]):

    for i in range(len(matriz)):
        if i == 0:
            minimo = matriz[i][2]
            garaje = i
        elif minimo > matriz[i][2]:
            minimo = matriz[i][2]
            garaje = i

    print(f'El garaje que almacena menos unidades es el {garaje + 1} con {minimo} unidades')




