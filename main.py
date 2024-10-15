from UTN_Heroes_Dataset.utn_pp import get_original_matrix, clear_console
from funciones.funciones import (obtener_existencias, mostrar_total_de_unidades_almacenadas, datos_garaje_con_menor_unidades, maxima_cantidad_almacenada, 
obtener_recaudacion, cantidad_garajes_mayor_unidades, porcentajes_de_unidades_por_marca, generar_informe_ganacias)
from funciones.auxiliares import cambiar_filas_por_columnas, validar_numero
from funciones.menu import mostrar_menu


matriz_concesionaria = cambiar_filas_por_columnas(get_original_matrix())
nombres_columnas = ['Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']

if __name__ == '__main__':
    
    while True:
        mostrar_menu()
        opcion = validar_numero(1,9)

        match opcion:
            case 1:
                obtener_existencias(matriz_concesionaria)
            case 2:
                mostrar_total_de_unidades_almacenadas(matriz_concesionaria)
            case 3:
                datos_garaje_con_menor_unidades(matriz_concesionaria)
            case 4:
                maxima_cantidad_almacenada(matriz_concesionaria)
            case 5: 
                obtener_recaudacion(matriz_concesionaria)
            case 6:
                cantidad_garajes_mayor_unidades(matriz_concesionaria)
            case 7:
                porcentajes_de_unidades_por_marca(matriz_concesionaria)
            case 8:
                generar_informe_ganacias(matriz_concesionaria)
            case 9:
                break

        clear_console()


