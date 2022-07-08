from typing import TypeVar
import math
import random
from dominio import Dominio

T = TypeVar('T')


def optimizar(dominio: Dominio, tam_pobl: int, porc_elite: float, prob_mut: float, reps: int) -> T:
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    tam_pobl (int)
        Tamaño de la población.

    porc_elite (float)
        Porcentaje de la población que se tomará como elite.

    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]

    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (T) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """
    solucion_posible = dominio.generar_n(tam_pobl)
    while reps > 0:
        contenedor_solucion = []
        for sol in solucion_posible:
            costo = dominio.fcosto(sol)
            contenedor_solucion.append((sol, costo))
        contenedor_solucion.sort(key=lambda x:x[1])
        padre = math.floor(tam_pobl*porc_elite)
        hijo = tam_pobl - padre

        generacion_siguiente = []
        descendencia = []

        for solucion_ordenada in contenedor_solucion[0:padre]:
            generacion_siguiente.append(solucion_ordenada[0])
        while hijo > 0:
            padre_indice = padre - 1

            primer_padre = generacion_siguiente[random.randint(0, padre_indice)]
            segundo_padre = generacion_siguiente[random.randint(0, padre_indice)]

            hijos = dominio.cruzar(primer_padre,segundo_padre)
            a = random.uniform(0,1)
            if prob_mut >= a:
                hijos = dominio.mutar(hijos)
            descendencia.append(hijos)
            hijo -= 1

        solucion_posible = generacion_siguiente + descendencia
        reps -= 1
    for sol in solucion_posible:
        costo = dominio.fcosto(sol)
        contenedor_solucion.append((sol,costo))
    contenedor_solucion.sort(key = lambda x:x[1])
    return  contenedor_solucion[0][0]


    # Pendiente: implementar este método

