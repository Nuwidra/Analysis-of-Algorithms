import big_o
from big_o import complexities as cmpl
import importlib
import math
import numpy as np
from random import shuffle
import unittest
import warnings

from rutas import contar_rutas_mas_cortas


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


def _generar(n):
    M = np.random.randint(2, size=(n, n))
    M[0][0] = 0
    M[-1][-1] = 0

    return M


class PruebasRutas(unittest.TestCase):

    def test_contar_rutas_mas_cortas_sin_solucion(self):
        C = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 1]]

        tam_Rs = contar_rutas_mas_cortas(C)
        self.assertEqual(tam_Rs, 0)

    def test_contar_rutas_mas_cortas_todas(self):
        C = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        tam_Rs = contar_rutas_mas_cortas(C)
        self.assertEqual(tam_Rs, 20)

    def test_contar_rutas_mas_cortas_con_intersecciones_peligrosas(self):
        C = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 0]]

        tam_Rs = contar_rutas_mas_cortas(C)
        self.assertEqual(tam_Rs, 4)

    def test_contar_rutas_mas_cortas_complejidad_xy(self):
        best, fitted = big_o.big_o(contar_rutas_mas_cortas, _generar, min_n=4, max_n=1000, n_measures=50, n_repeats=3, classes=[
            cmpl.Linear, cmpl.Logarithmic, cmpl.Linearithmic, cmpl.Quadratic, cmpl.Cubic], verbose=False, return_raw_data=True)

        _graficar(fitted, 'contar_rutas_mas_cortas')

        if not isinstance(best, big_o.complexities.Quadratic):
            warnings.warn(
                f'Complejidad esperada Cuadrática, complejidad estimada {best}')
