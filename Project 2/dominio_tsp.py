import random

import csv_reader
from dominio import Dominio
from typing import List
from random import randint
from csv_reader import obtenerInformacion


class DominioTSP(Dominio):
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.

    Las soluciones se modelan como listas de enteros, donde cada número representa
    una ciudad específica. Si el grafo contiene n ciudades, la lista siempre contiene
    (n-1) elementos. La lista nunca contiene elementos repetidos y nunca contiene la 
    ciudad de inicio y fin del circuito.

    Métodos:
    generar() -> List[int]
        Construye aleatoriamente una estructura de datos que representa una posible 
        solución al problema.

    fcosto(sol: List[int]) -> float
        Calcula el costo asociado con una solución dada.

    vecino(sol: List[int]) -> List[int]
        Calcula una solución vecina a partir de una solución dada.

    validar(sol: List[int]) -> bool
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol: List[int]) -> str
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

    generar_n(n: int) -> List[T]
        Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

    cruzar(sol_a: List[int], sol_b: List[int]) -> List[int]
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol: List[int]) -> List[int]
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    def __init__(self, ciudades_rutacsv: str, ciudad_inicio: str) -> None:
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """
        self.ciudades_rutascsv = obtenerInformacion(ciudades_rutacsv)
        self.ciudad_inicio = ciudad_inicio


    def validar(self, sol: List[int]) -> bool:
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (List[int])
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """
        n = len(self.ciudades_rutascsv) - 2
        idxCiudadInicio = self.ciudades_rutascsv[0].index(self.ciudad_inicio) - 1
        
        if len(sol) != n:
            return False
        
        if max(sol) > n:
            return False 
        
        if len(sol) != len(set(sol)):
            return False
        
        if idxCiudadInicio in sol:
            return False

        return True
        
    def texto(self, sol: List[int]) -> str:
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (List[int])
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """
        final = ""
        final += self.ciudad_inicio + " -> "
        
        for i in sol:
            ciudad = self.ciudades_rutascsv[0][i + 1]
            final = final + ciudad + " -> "
        
        final += self.ciudad_inicio
        
        return final

    def generar(self) -> List[int]:
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (List[int]) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        lista = []
        ciudadInicio = self.ciudades_rutascsv[0].index(self.ciudad_inicio) - 1

        for i in range(0, len(self.ciudades_rutascsv) - 1):
            if i != ciudadInicio:
                lista.append(i)

        return random.sample(lista, len(lista))

    def fcosto(self, sol: List[int]) -> float:
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (List[int])
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """
        ciudadInicio = self.ciudades_rutascsv[0].index(self.ciudad_inicio) - 1
        print(ciudadInicio)
        ciudadOrigen = ciudadInicio
        costoFinal = 0

        for elem in sol:
            costo = float(self.ciudades_rutascsv[ciudadOrigen + 1][elem + 1])
            print(elem, costo)
            costoFinal += costo
            ciudadOrigen = elem

        costoFinal += float(self.ciudades_rutascsv[ciudadOrigen + 1][ciudadInicio + 1])

        return costoFinal


    def vecino(self, sol: List[int]) -> List[int]:
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (List[int])
            Solución a partir de la cual se originará una nueva solución vecina

        Salidas:
        (List[int]) Solución vecina
        """
        vecino = list(sol)

        rango = range(len(sol))
        i,j = random.sample(rango,2)
        sol[i], sol[j] = sol[j], sol[i]
        return vecino
    


    def generar_n(self, n: int) -> List[List[int]]:
        """Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (List[int]) Lista que contiene n estructuras de datos, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """
        lt = []
        lista = []
        ciudadInicio = self.ciudades_rutascsv[0].index(self.ciudad_inicio) - 1

        for i in range(0, len(self.ciudades_rutascsv) - 1):
            if i != ciudadInicio:
                lista.append(i)

        for i in range(n):
            j = random.sample(lista, len(lista))
            lt.append(j)

        return lt


    def cruzar(self, sol_a: List[int], sol_b: List[int]) -> List[int]:
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (List[int])
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (List[int])
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (List[int]) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """
        elementos = []
        hijo = []
        counter = 0

        for i in range(0, len(sol_a)):
            hijo.append(-1)

        for i in range(0, len(sol_a) // 2):
            while True:
                randomIdx = randint(0, len(sol_b) - 1)
                if sol_b[randomIdx] not in elementos:
                    break
            ciudad = sol_b[randomIdx]
            elementos.append(ciudad)
            hijo[randomIdx] = ciudad

        for i in range(0, len(sol_a)):
            if hijo[i] == -1:
                while True:
                    elem1 = sol_a[counter]
                    counter += 1
                    if (elem1 not in elementos):
                        hijo[i] = elem1
                        break
        print(sol_a, sol_b)
        print(hijo)
        return hijo

    def mutar(self, sol: List[int]) -> List[int]:
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (List[int])
            La solución a mutar.

        Salidas:
        (List[int]) Una nueva solución que refleja un ligero cambio con respecto
        a la solución dada por parámetro
        """
        cantCambios = randint(1, len(sol) - 1)
        while cantCambios % 2 == 0:
            cantCambios = randint(1, len(sol) - 1)
        mutada = sol.copy()
        while cantCambios > 0:
            pos1 = randint(1, len(sol) - 1)
            pos2 = randint(1, len(sol) - 1)
            while pos1 == pos2:
                pos2 = randint(1, len(sol) - 1)
            mutada[pos1], mutada[pos2] = mutada[pos2], mutada[pos1]
            cantCambios -= 1

        return mutada
