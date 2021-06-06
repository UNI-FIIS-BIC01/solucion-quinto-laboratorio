from typing import List
from unittest import TestCase

from permutacion import obtener_permutaciones


class PermutacionTest(TestCase):

    def test_permutacion_con_duplicados(self):
        cadena_entrada: str = "ABCB"
        resultado_actual: List[str] = obtener_permutaciones(cadena_entrada)
        resultado_esperado: List[str] = ["ABCB",
                                         "BACB",
                                         "CABB",
                                         "ACBB",
                                         "BCAB",
                                         "CBAB",
                                         "CBBA",
                                         "BCBA",
                                         "BBCA",
                                         "BABC",
                                         "ABBC",
                                         "BBAC"]

        self.assertEqual(sorted(resultado_actual), sorted(resultado_esperado))

    def test_permutacion_sin_duplicados(self):
        cadena_entrada: str = "ABCD"
        resultado_actual: List[str] = obtener_permutaciones(cadena_entrada)
        resultado_esperado: List[str] = ["ABCD",
                                         "BACD",
                                         "CABD",
                                         "ACBD",
                                         "BCAD",
                                         "CBAD",
                                         "CBDA",
                                         "BCDA",
                                         "DCBA",
                                         "CDBA",
                                         "BDCA",
                                         "DBCA",
                                         "DACB",
                                         "ADCB",
                                         "CDAB",
                                         "DCAB",
                                         "ACDB",
                                         "CADB",
                                         "BADC",
                                         "ABDC",
                                         "DBAC",
                                         "BDAC",
                                         "ADBC",
                                         "DABC"]

        self.assertEqual(sorted(resultado_actual), sorted(resultado_esperado))
