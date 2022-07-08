import big_o
from big_o import complexities as cmpl
import importlib
import math
import numpy as np
from random import shuffle
import unittest
import warnings

from almacenamiento import maximizar


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
    K = 1024
    G = 1024 * 1024 * 1024
    return [(i, ti) for i, ti in enumerate(np.random.randint(1 * K, 10 * G, size=n))]


class PruebasAlmacenamiento(unittest.TestCase):

    def test_maximizar(self):
        As = [('archivo1', 10), ('archivo2', 5), ('archivo3', 3),
              ('archivo4', 8), ('archivo5', 9), ('archivo6', 1)]
        D = 10

        M = maximizar(As, D)
        self.assertListEqual(
            M, [('archivo6', 1), ('archivo3', 3), ('archivo2', 5)])

    def test_maximizar_complejidad_nlogn(self):
        best, fitted = big_o.big_o(lambda As: maximizar(As, np.random.randint(1024**3 * 10 * len(As) // 2)), _generar, min_n=4, max_n=10000, n_measures=1000, n_repeats=3, classes=[
            cmpl.Linear, cmpl.Logarithmic, cmpl.Linearithmic, cmpl.Quadratic, cmpl.Cubic], verbose=False, return_raw_data=True)

        _graficar(fitted, 'maximizar')

        if not isinstance(best, big_o.complexities.Linearithmic):
            warnings.warn(
                f'Complejidad esperada Linearítmica, complejidad estimada {best}')
