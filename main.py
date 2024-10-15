from UTN_Heroes_Dataset.utn_pp import get_original_matrix, mostrar_matriz_texto_tabla, clear_console, color_text
from funciones.funciones import obtener_existencias
from funciones.auxiliares import cambiar_filas_por_columnas

matriz_concesionaria = cambiar_filas_por_columnas(get_original_matrix())
nombres_columnas = ['Marca', 'Modelo', 'Unidades', 'Precio', 'Ganancia']

if __name__ == '__main__':
    
    mostrar_matriz_texto_tabla(matriz_concesionaria, nombres_columnas)
    obtener_existencias(matriz_concesionaria)

    

