import unittest

from rutas import encontrar_ruta


class PruebasRutas(unittest.TestCase):

    def test_encontrar_ruta_sin_solucion(self):
        C = [[0, 1, 1, 1],
             [0, 0, 0, 0],
             [1, 0, 1, 0],
             [1, 0, 1, 1],
             [0, 0, 1, 0]]

        R = encontrar_ruta(C)
        self.assertEqual(R, [])

    def test_encontrar_ruta_una_solucion_posible(self):
        C = [[0, 1, 1, 1],
             [0, 0, 1, 0],
             [1, 0, 1, 0],
             [1, 0, 1, 1],
             [0, 0, 0, 0]]

        E = [[1, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 1]]

        R = encontrar_ruta(C)
        self.assertListEqual(R, E)

    def test_encontrar_ruta_un_posible_retorno(self):
        C = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 1, 0, 1],
             [1, 1, 0, 0]]

        E1 = [[1, 1, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 1]]

        E2 = [[1, 1, 1, 1],
              [0, 0, 0, 1],
              [0, 0, 1, 1],
              [0, 0, 1, 0],
              [0, 0, 1, 1]]

        E3 = [[1, 1, 1, 1],
              [0, 0, 1, 1],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 1]]

        E4 = [[1, 1, 1, 0],
              [0, 0, 1, 1],
              [0, 0, 1, 1],
              [0, 0, 1, 0],
              [0, 0, 1, 1]]

        R = encontrar_ruta(C)
        self.assertTrue(R == E1 or R == E2 or R == E3 or R == E4)

    def test_encontrar_ruta_varias_soluciones_posibles(self):
        C = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]

        E1 = [[1, 1, 1, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 1],
              [0, 0, 0, 1]]

        E2 = [[1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 0, 0, 0],
              [1, 1, 1, 1]]

        R = encontrar_ruta(C)

        self.assertTrue(R == E1 or R == E2)

    def test_encontrar_ruta_complejo(self):
        C = [[0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1],
             [0, 1, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 1, 0]]

        E = [[1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 1]]

        R = encontrar_ruta(C)
        self.assertListEqual(R, E)
