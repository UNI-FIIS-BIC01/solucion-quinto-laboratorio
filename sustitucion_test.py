from typing import Dict
from unittest import TestCase

from desplazamiento import cargar_diccionario
from sustitucion import construir_diccionario_sustitucion, CodificadorPorSustitucion, DecodificadorPorSustitucion


class SustitucionTest(TestCase):

    def test_construir_diccionario_sustitucion(self):
        diccionario_esperado: Dict[str, str] = {'A': 'E',
                                                'B': 'B',
                                                'C': 'C',
                                                'D': 'D',
                                                'E': 'A',
                                                'F': 'F',
                                                'G': 'G',
                                                'H': 'H',
                                                'I': 'I',
                                                'J': 'J',
                                                'K': 'K',
                                                'L': 'L',
                                                'M': 'M',
                                                'N': 'N',
                                                'O': 'U',
                                                'P': 'P',
                                                'Q': 'Q',
                                                'R': 'R',
                                                'S': 'S',
                                                'T': 'T',
                                                'U': 'O',
                                                'V': 'V',
                                                'W': 'W',
                                                'X': 'X',
                                                'Y': 'Y',
                                                'Z': 'Z',
                                                'a': 'e',
                                                'b': 'b',
                                                'c': 'c',
                                                'd': 'd',
                                                'e': 'a',
                                                'f': 'f',
                                                'g': 'g',
                                                'h': 'h',
                                                'i': 'i',
                                                'j': 'j',
                                                'k': 'k',
                                                'l': 'l',
                                                'm': 'm',
                                                'n': 'n',
                                                'o': 'u',
                                                'p': 'p',
                                                'q': 'q',
                                                'r': 'r',
                                                's': 's',
                                                't': 't',
                                                'u': 'o',
                                                'v': 'v',
                                                'w': 'w',
                                                'x': 'x',
                                                'y': 'y',
                                                'z': 'z'}

        self.assertEqual(construir_diccionario_sustitucion("eaiuo"), diccionario_esperado)

    def test_codificador_sustitucion(self):
        diccionario_esperado: Dict[str, str] = {'A': 'E',
                                                'B': 'B',
                                                'C': 'C',
                                                'D': 'D',
                                                'E': 'A',
                                                'F': 'F',
                                                'G': 'G',
                                                'H': 'H',
                                                'I': 'I',
                                                'J': 'J',
                                                'K': 'K',
                                                'L': 'L',
                                                'M': 'M',
                                                'N': 'N',
                                                'O': 'U',
                                                'P': 'P',
                                                'Q': 'Q',
                                                'R': 'R',
                                                'S': 'S',
                                                'T': 'T',
                                                'U': 'O',
                                                'V': 'V',
                                                'W': 'W',
                                                'X': 'X',
                                                'Y': 'Y',
                                                'Z': 'Z',
                                                'a': 'e',
                                                'b': 'b',
                                                'c': 'c',
                                                'd': 'd',
                                                'e': 'a',
                                                'f': 'f',
                                                'g': 'g',
                                                'h': 'h',
                                                'i': 'i',
                                                'j': 'j',
                                                'k': 'k',
                                                'l': 'l',
                                                'm': 'm',
                                                'n': 'n',
                                                'o': 'u',
                                                'p': 'p',
                                                'q': 'q',
                                                'r': 'r',
                                                's': 's',
                                                't': 't',
                                                'u': 'o',
                                                'v': 'v',
                                                'w': 'w',
                                                'x': 'x',
                                                'y': 'y',
                                                'z': 'z'}
        codificador: CodificadorPorSustitucion = CodificadorPorSustitucion("Hello World!", "eaiuo")

        self.assertEqual("Hello World!", codificador.get_texto_mensaje())
        self.assertEqual(diccionario_esperado, codificador.get_diccionario_sustitucion())
        self.assertEqual("Hallu Wurld!", codificador.get_mensaje_encriptado())

    def test_decodificador_sustitucion(self):
        decodificador: DecodificadorPorSustitucion = DecodificadorPorSustitucion("Boanus dies, qoaridu prufasur!")
        self.assertEqual("Buenos dias, querido profesor!", decodificador.descifrar_mensaje())
        self.assertEqual(cargar_diccionario("diccionario.txt"), decodificador.get_diccionario())
