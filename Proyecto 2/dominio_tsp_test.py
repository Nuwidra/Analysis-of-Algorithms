from math import ceil
import unittest

from dominio_tsp import DominioTSP


class PruebaDominioTSP(unittest.TestCase):

    __tsp = None

    @classmethod
    def setUpClass(cls):
        cls.__tsp = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')

    def test_constructor(self):
        tsp = DominioTSP('datos/ciudades_cr_pruebas.csv', 'Alajuela')
        self.assertIsNotNone(tsp)

    def test_validar_correcta(self):
        self.assertTrue(self.__tsp.validar([1, 2, 3]))

    def test_validar_mas_ciudades(self):
        self.assertTrue(self.__tsp.validar([1, 2, 3, 4]) == False)

    def test_validar_ciudad_inexistente(self):
        self.assertTrue(self.__tsp.validar([1, 4, 3]) == False)

    def test_validar_con_ciudad_inicial(self):
        self.assertTrue(self.__tsp.validar([0, 2, 3]) == False)

    def test_validar_menos_ciudades(self):
        self.assertTrue(self.__tsp.validar([2, 3]) == False)

    def test_validar_ciudades_repetidas(self):
        self.assertTrue(self.__tsp.validar([1, 2, 1]) == False)

    def test_texto(self):
        self.assertEqual(self.__tsp.texto(
            [1, 2, 3]), "Alajuela -> Heredia -> San José -> Cartago -> Alajuela")

    def test_generar(self):
        n = 10
        repetidos = 0
        sol = self.__tsp.generar()
        for _ in range(n):
            self.assertTrue(self.__tsp.validar(sol))
            nueva_sol = self.__tsp.generar()
            if (sol == nueva_sol):
                repetidos += 1

        self.assertNotEqual(n, repetidos)

    def test_fcosto(self):
        costo = self.__tsp.fcosto([1, 2, 3])
        self.assertEqual(costo, 121.2)

    def test_vecino(self):
        sol = self.__tsp.generar()
        vecino = self.__tsp.vecino(sol)
        # las soluciones no deben ser iguales
        self.assertNotEqual(sol, vecino)

    def test_generar_n(self):
        soluciones = self.__tsp.generar_n(10)
        self.assertEqual(len(soluciones), 10)
        for sol in soluciones:
            self.assertTrue(self.__tsp.validar(sol))

    def test_cruzar(self):
        sol_a, sol_b = self.__tsp.generar_n(2)
        hija = self.__tsp.cruzar(sol_a, sol_b)
        print(sol_a, sol_b, hija)
        self.assertTrue(self.__tsp.validar(hija))

    def test_mutar(self):
        sol = self.__tsp.generar()
        mutada = self.__tsp.mutar(sol)
        # las soluciones no deben ser iguales
        self.assertNotEqual(sol, mutada)
