import big_o
from big_o import complexities as cmpl
import importlib
import math
import numpy as np
import unittest
import warnings

import sumatoria


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


class PruebasSumatoria(unittest.TestCase):

    def test_sumatoria_cubica(self):
        ns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        fs = [0, 2, 8, 20, 40, 70, 112, 168, 240, 330, 440, 572, 910, 1938, 2660, 4600, 8990, 10912, 18278, 24682,
              28380, 36848, 52470, 71980, 79422, 104788, 124392, 135050, 170640, 197540, 242970, 313698, 353702]

        rs = [sumatoria.sumatoria_cubica(n) for n in ns]
        self.assertListEqual(rs, fs)

    def test_compl_sumatoria_cubica(self):
        print()
        best, fitted = big_o.big_o(sumatoria.sumatoria_cubica, big_o.datagen.n_, min_n=1, max_n=100,
                                   n_measures=100, n_repeats=3, verbose=False,
                                   classes=[cmpl.Linear, cmpl.Quadratic, cmpl.Constant, cmpl.Cubic], return_raw_data=True)

        _graficar(fitted, 'sumatoria_cubica')

        if not isinstance(best, big_o.complexities.Cubic):
            warnings.warn(
                f'Complejidad esperada Cúbica, complejidad estimada {best}')

    def test_sumatoria_constante(self):
        ns = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 29,
              31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        fs = [0, 2, 8, 20, 40, 70, 112, 168, 240, 330, 440, 572, 910, 1938, 2660, 4600, 8990, 10912, 18278, 24682,
              28380, 36848, 52470, 71980, 79422, 104788, 124392, 135050, 170640, 197540, 242970, 313698, 353702]

        rs = [sumatoria.sumatoria_constante(n) for n in ns]
        self.assertListEqual(rs, fs)

    def test_compl_sumatoria_constante(self):
        print()
        best, fitted = big_o.big_o(sumatoria.sumatoria_constante, big_o.datagen.n_, min_n=1, max_n=10000,
                                   n_measures=10000, n_repeats=3, n_timings=5, verbose=False,
                                   classes=[cmpl.Constant, cmpl.Quadratic], return_raw_data=True)

        _graficar(fitted, 'sumatoria_constante')

        if not isinstance(best, big_o.complexities.Constant):
            warnings.warn(
                f'Complejidad esperada Constante, complejidad estimada {best}')
