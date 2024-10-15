from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
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

#4 - Máxima cantidad de unidades almacenadas entre todos los garajes.

def maxima_cantidad_almacenada(matriz: list[list]):

    for i in range(len(matriz)):
        if i == 0:
            maximo = matriz[i][2]
        elif maximo < matriz[i][2]:
            maximo = matriz[i][2]
    
    print(f'La cantidad maxima almacenada en un solo garaje es de {maximo} vehiculos')

#5 - Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, 
# teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.

def obtener_recaudacion(matriz: list[list]):

    for i in range(len(matriz)):
        matriz[i][4] = matriz[i][2] * matriz[i][3]
        print(f'La recaudacion del garaje {i + 1} es de {matriz[i][4]}')

#6 - Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.

def cantidad_garajes_mayor_unidades(matriz: list[list]):

    total_garajes = 0
    for i in range(len(matriz)):
        if matriz[i][2] >= 6:
            total_garajes += 1

    print(f'La cantidad de garajes con 6 o mas unidades es {total_garajes}')

#7 - Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados entre todos los garajes de la sede matriz. 
# Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.

def porcentajes_de_unidades_por_marca(matriz: list[list]):

    marcas = []
    for i in range(len(matriz)):
        if matriz[i][0] not in marcas:
            marcas.append(matriz[i][0])
    
    total_unidades_por_marca = [0] * len(marcas)
    total_unidades_en_concesionaria = 0

    for i in range(len(matriz)):
        for j in range(len(marcas)):
            if matriz[i][0] == marcas[j]:
                total_unidades_por_marca[j] += matriz[i][2]
        total_unidades_en_concesionaria += matriz[i][2]

    for i in range(len(matriz)):
        for j in range(len(marcas)):
            if matriz[i][0] == marcas[j]:
                maximo_porcentaje_garaje_por_marca = matriz[i][2] / total_unidades_por_marca[j] * 100
                garaje_maximo_porcentaje = i
            elif maximo_porcentaje_garaje_por_marca < (matriz[i][2] / total_unidades_por_marca[j] * 100):
                maximo_porcentaje_garaje_por_marca = matriz[i][2] / total_unidades_por_marca[j] * 100
                garaje_maximo_porcentaje = i

    for i in range(len(marcas)):
        print(f'La marca {marcas[i]} tiene un porcentaje de {total_unidades_por_marca[i] / total_unidades_en_concesionaria * 100} sobre el total de vehiculos almacenados en la concesionaria')

    print(f"""El garaje con mayor porcentaje de su marca es el {garaje_maximo_porcentaje + 1}
Marca: {matriz[garaje_maximo_porcentaje][0]}
Modelo: {matriz[garaje_maximo_porcentaje][1]}
Unidades: {matriz[garaje_maximo_porcentaje][2]}
Precio: {matriz[garaje_maximo_porcentaje][3]}
Ganancia: {matriz[garaje_maximo_porcentaje][4]}
""")
    
#8 - Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.

def generar_informe_ganacias(matriz: list[list]):

    for i in range(len(matriz) - 1):
        for j in range(i + 1, len(matriz)):
            if matriz[i][4] < matriz[j][4]:
                matriz[i][0], matriz[j][0] = matriz[j][0], matriz[i][0]
                matriz[i][1], matriz[j][1] = matriz[j][1], matriz[i][1]
                matriz[i][2], matriz[j][2] = matriz[j][2], matriz[i][2]
                matriz[i][3], matriz[j][3] = matriz[j][3], matriz[i][3]
                matriz[i][4], matriz[j][4] = matriz[j][4], matriz[i][4]

    nombres_columnas = ['Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']
    mostrar_matriz_texto_tabla(matriz, nombres_columnas)




