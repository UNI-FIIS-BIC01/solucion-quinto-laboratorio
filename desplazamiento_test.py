from typing import Dict
from unittest import TestCase

from desplazamiento import CodificadorPorDesplazamiento, construir_diccionario_desplazamiento, aplicar_diccionario_encriptado, \
    DecodificadorPorDesplazamiento, cargar_diccionario


class DesplazamientoTest(TestCase):

    def test_construir_diccionario_desplazamiento(self):
        diccionario_esperado: Dict[str, str] = {'a': 'c', 'A': 'C', 'b': 'd', 'B': 'D', 'c': 'e', 'C': 'E', 'd': 'f',
                                                'D': 'F',
                                                'e': 'g', 'E': 'G', 'f': 'h', 'F': 'H', 'g': 'i', 'G': 'I', 'h': 'j',
                                                'H': 'J',
                                                'i': 'k', 'I': 'K', 'j': 'l', 'J': 'L', 'k': 'm', 'K': 'M', 'l': 'n',
                                                'L': 'N',
                                                'm': 'o', 'M': 'O', 'n': 'p', 'N': 'P', 'o': 'q', 'O': 'Q', 'p': 'r',
                                                'P': 'R',
                                                'q': 's', 'Q': 'S', 'r': 't', 'R': 'T', 's': 'u', 'S': 'U', 't': 'v',
                                                'T': 'V',
                                                'u': 'w', 'U': 'W', 'v': 'x', 'V': 'X', 'w': 'y', 'W': 'Y', 'x': 'z',
                                                'X': 'Z',
                                                'y': 'a', 'Y': 'A', 'z': 'b', 'Z': 'B'}

        self.assertEqual(construir_diccionario_desplazamiento(2), diccionario_esperado)

    def test_aplicar_diccionario_encripcion(self):
        diccionario_encriptado: Dict[str, str] = {'a': 'c', 'A': 'C', 'b': 'd', 'B': 'D', 'c': 'e', 'C': 'E', 'd': 'f',
                                                  'D': 'F',
                                                  'e': 'g', 'E': 'G', 'f': 'h', 'F': 'H', 'g': 'i', 'G': 'I', 'h': 'j',
                                                  'H': 'J',
                                                  'i': 'k', 'I': 'K', 'j': 'l', 'J': 'L', 'k': 'm', 'K': 'M', 'l': 'n',
                                                  'L': 'N',
                                                  'm': 'o', 'M': 'O', 'n': 'p', 'N': 'P', 'o': 'q', 'O': 'Q', 'p': 'r',
                                                  'P': 'R',
                                                  'q': 's', 'Q': 'S', 'r': 't', 'R': 'T', 's': 'u', 'S': 'U', 't': 'v',
                                                  'T': 'V',
                                                  'u': 'w', 'U': 'W', 'v': 'x', 'V': 'X', 'w': 'y', 'W': 'Y', 'x': 'z',
                                                  'X': 'Z',
                                                  'y': 'a', 'Y': 'A', 'z': 'b', 'Z': 'B'}
        self.assertEqual("jgnnq", aplicar_diccionario_encriptado("hello", diccionario_encriptado))

    def test_codificador_desplazamiento(self):
        codificador: CodificadorPorDesplazamiento = CodificadorPorDesplazamiento("hello", 2)
        diccionario_esperado: Dict[str, str] = {'a': 'c', 'A': 'C', 'b': 'd', 'B': 'D', 'c': 'e', 'C': 'E', 'd': 'f',
                                                'D': 'F',
                                                'e': 'g', 'E': 'G', 'f': 'h', 'F': 'H', 'g': 'i', 'G': 'I', 'h': 'j',
                                                'H': 'J',
                                                'i': 'k', 'I': 'K', 'j': 'l', 'J': 'L', 'k': 'm', 'K': 'M', 'l': 'n',
                                                'L': 'N',
                                                'm': 'o', 'M': 'O', 'n': 'p', 'N': 'P', 'o': 'q', 'O': 'Q', 'p': 'r',
                                                'P': 'R',
                                                'q': 's', 'Q': 'S', 'r': 't', 'R': 'T', 's': 'u', 'S': 'U', 't': 'v',
                                                'T': 'V',
                                                'u': 'w', 'U': 'W', 'v': 'x', 'V': 'X', 'w': 'y', 'W': 'Y', 'x': 'z',
                                                'X': 'Z',
                                                'y': 'a', 'Y': 'A', 'z': 'b', 'Z': 'B'}

        self.assertEqual(2, codificador.get_desplazamiento())
        self.assertEqual(diccionario_esperado, codificador.get_diccionario_desplazamiento())
        self.assertEqual("jgnnq", codificador.get_mensaje_encriptado())

        codificador.cambiar_desplazamiento(1)
        diccionario_esperado: Dict[str, str] = {'a': 'b', 'A': 'B', 'b': 'c', 'B': 'C', 'c': 'd', 'C': 'D', 'd': 'e',
                                                'D': 'E',
                                                'e': 'f', 'E': 'F', 'f': 'g', 'F': 'G', 'g': 'h', 'G': 'H', 'h': 'i',
                                                'H': 'I',
                                                'i': 'j', 'I': 'J', 'j': 'k', 'J': 'K', 'k': 'l', 'K': 'L', 'l': 'm',
                                                'L': 'M',
                                                'm': 'n', 'M': 'N', 'n': 'o', 'N': 'O', 'o': 'p', 'O': 'P', 'p': 'q',
                                                'P': 'Q',
                                                'q': 'r', 'Q': 'R', 'r': 's', 'R': 'S', 's': 't', 'S': 'T', 't': 'u',
                                                'T': 'U',
                                                'u': 'v', 'U': 'V', 'v': 'w', 'V': 'W', 'w': 'x', 'W': 'X', 'x': 'y',
                                                'X': 'Y',
                                                'y': 'z', 'Y': 'Z', 'z': 'a', 'Z': 'A'}

        self.assertEqual(1, codificador.get_desplazamiento())
        self.assertEqual("hello", codificador.get_texto_mensaje())
        self.assertEqual(diccionario_esperado, codificador.get_diccionario_desplazamiento())
        self.assertEqual("ifmmp", codificador.get_mensaje_encriptado())

    def test_decodificador_desplazamiento(self):
        decodificador: DecodificadorPorDesplazamiento = DecodificadorPorDesplazamiento("jqnc")
        self.assertEqual((2, "hola"), decodificador.descifrar_mensaje())
        self.assertEqual(cargar_diccionario("diccionario.txt"), decodificador.get_diccionario())
