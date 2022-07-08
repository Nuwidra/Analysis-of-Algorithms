import big_o
from big_o import complexities as cmpl
import importlib
import math
import numpy as np
from random import shuffle
import unittest
import warnings

from burbuja import burbuja, burbuja_optimizado


def _graficar(fitted, titulo):
    xs = fitted['measures']
    ys = fitted['times']

    if importlib.util.find_spec('gnuplotlib') is not None:
        import gnuplotlib as gp
        gp.plot(xs, ys, _with='lines', terminal='dumb 60,30',
                unset='grid', title=titulo, xlabel='n', ylabel='tiempo')

    for k, v in fitted.items():
        if isinstance(k, big_o.complexities.ComplexityClass):
            residual = v
            r2 = 1 - residual / (ys.size * ys.var())
            print(k, f' (r={residual}, r^2={r2})')


def _comparar_curvas(fitted_a, fitted_b):
    xs_a = fitted_a['measures']
    ys_a = fitted_a['times']
    xs_b = fitted_b['measures']
    ys_b = fitted_b['times']

    if importlib.util.find_spec('gnuplotlib') is not None:
        import gnuplotlib as gp
        gp.plot((xs_a, ys_a), (xs_b, ys_b), _with='lines', terminal='dumb 60,30',
                unset='grid', title='Comparación', xlabel='n', ylabel='tiempo')


def generar_aleatorio(n):
    A = list(range(0, n))
    shuffle(A)

    return A

#---------------------------------------
#       Funciones Generadoras
#---------------------------------------
def generar_mejor(n):
    A = list(range(0, n))
    shuffle(A)
    return A

def generar_peor(n):
    A = list(range(n, 0, -1))
    return A

def generar_promedio(n):
    A = list(range(0, n))
    shuffle(A)
    return A

class PruebasBurbuja(unittest.TestCase):

    def test_burbuja(self):
        A = [5, 3, 9, 0, 6, 2, 8, 1, 4, 7]
        burbuja(A)

        self.assertListEqual(A, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_burbuja_cuadratica(self):
        print()
        best, fitted = big_o.big_o(burbuja, generar_aleatorio, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, 'burbuja')

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')

    def test_burbuja_optimizado(self):
        A = [5, 3, 9, 0, 6, 2, 8, 1, 4, 7]
        burbuja_optimizado(A)

        self.assertListEqual(A, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


    def test_comparacion(self):
        _, fitted = big_o.big_o(burbuja, generar_aleatorio, min_n=10, max_n=1000,
                                n_measures=100, n_repeats=3, verbose=False,
                                classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _, fitted_o = big_o.big_o(burbuja_optimizado, generar_aleatorio, min_n=10, max_n=1000,
                                  n_measures=100, n_repeats=3, verbose=False,
                                  classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _comparar_curvas(fitted, fitted_o)

        self.assertLessEqual(fitted_o['times'][-1], fitted['times'][-1])

    #--------------------------------------------------
    # Test
    #--------------------------------------------------
    def test_mejor_caso(self):
        print()
        best, fitted = big_o.big_o(burbuja, generar_mejor, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, 'Mejor Caso')

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')

    def test_peor_caso(self):
        print()
        best, fitted = big_o.big_o(burbuja, generar_peor, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, 'Peor Caso')

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')

    def test_caso_promedio(self):
        print()
        best, fitted = big_o.big_o(burbuja, generar_promedio, min_n=10, max_n=1000,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linear, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, 'Caso Promedio')

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')
