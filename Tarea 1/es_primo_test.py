import big_o
from big_o import complexities as cmpl
import importlib
import math
import numpy as np
import unittest
import warnings

from es_primo import es_primo


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


class PruebasEsPrimo(unittest.TestCase):

    def test_es_primo(self):
        self.assertFalse(es_primo(1))
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertFalse(es_primo(8))
        self.assertFalse(es_primo(980))
        self.assertTrue(es_primo(7841))
        self.assertTrue(es_primo(16127))
        self.assertTrue(es_primo(65537))


    def test_compl_es_primo(self):
        print()
        best, fitted = big_o.big_o(es_primo, big_o.datagen.n_, min_n=1, max_n=10000,
                                   n_measures=100, n_repeats=3, verbose=False, classes=[], return_raw_data=True)

        _graficar(fitted, 'es_primo')


