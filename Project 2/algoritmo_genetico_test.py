import unittest

from algoritmo_genetico import optimizar
from dominio_tsp import DominioTSP

class PruebaAlgoritmoGenetico(unittest.TestCase):

    def test_optimizar(self):
        dominio = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')
        sol = optimizar(dominio, 10000, 0.1, 0.1, 1000)
        self.assertTrue(dominio.validar(sol))
        self.assertAlmostEqual(dominio.fcosto(sol), 121.2)
