from abc import ABC
from abc import abstractmethod
from typing import Generic
from typing import List
from typing import TypeVar

T = TypeVar('T')


class Dominio(ABC, Generic[T]):
    """
    Representa el objeto de dominio que conoce los detalles de implementación y modelamiento
    de algún problema específico para ser resuelto con algoritmos probabilísticos.

    Métodos:
    generar() -> T
        Construye aleatoriamente una estructura de datos que representa una posible 
        solución al problema.

    fcosto(sol: T) -> float
        Calcula el costo asociado con una solución dada.

    vecino(sol: T) -> T
        Calcula una solución vecina a partir de una solución dada.

    validar(sol: T) -> bool
        Valida que la solución dada cumple con los requisitos del problema.

    texto(sol: T) -> str
        Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

    generar_n(n: int) -> List[T]
        Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

    cruzar(sol_a: T, sol_b: T) -> T
        Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

    mutar(sol: T) -> T
        Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.
    """

    @abstractmethod
    def generar(self) -> T:
        """Construye una estructura de datos que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        Una estructura de datos que representa una posible solución válida al problema
        """

        pass

    @abstractmethod
    def fcosto(self, sol: T) -> float:
        """Calcula el costo asociado con una solución dada.

        Entradas:
        sol (estructura de datos)
            Solución cuyo costo se debe calcular

        Salidas:
        (float) valor del costo asociado con la solución
        """

        pass

    @abstractmethod
    def vecino(self, sol: T) -> T:
        """Calcula una solución vecina a partir de una solución dada.

        Una solución vecina comparte la mayor parte de su estructura con 
        la solución que la origina, aunque no son exactamente iguales. El 
        método transforma aleatoriamente algún aspecto de la solución
        original.

        Entradas:
        sol (estructura de datos)
            Solución a partir de la cual se calculará una nueva solución vecina.

        Salidas:
        (estructura de datos) nueva solución construida con base en la solución de la entrada.
        """
        pass

    @abstractmethod
    def validar(self, sol: T) -> bool:
        """Valida que la solución dada cumpla con todos los requerimientos del problema.

        Entradas:
        sol (estructura de datos)
            La solución a validar

        Salidas:
        (bool) True si la solución es valida, False en cualquier otro caso.
        """

        pass

    @abstractmethod
    def texto(self, sol: T) -> str:
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        Entradas:
        sol (estructura de datos)
            La solución a transformar en texto legible

        Salidas:
        (str) El texto legible que representa a la solución.
        """

        pass

    @abstractmethod
    def generar_n(self, n: int) -> List[T]:
        """Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (list) Lista que contiene n estructuras de datos, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """

        pass

    @abstractmethod
    def cruzar(self, sol_a: T, sol_b: T) -> T:
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro.

        Entradas:
        sol_a (estructura de datos)
            Estructura de datos que modela la solución antecesora A que será cruzada con la B

        sol_b (estructura de datos)
            Estructura de datos que modela la solución antecesora B que será cruzada con la A

        Salidas:
        (estructura de datos) Una nueva solución producto del cruzamiento entre las soluciones A y B
        """

        pass

    @abstractmethod
    def mutar(self, sol: T) -> T:
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por
        parámetro.

        Entradas:
        sol (estructura de datos)
            La solución a mutar.

        Salidas:
        (estructura de datos) Una nueva solución que refleja un ligero cambio con respecto 
        a la solución dada por parámetro
        """

        pass
