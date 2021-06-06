import string

from desplazamiento import aplicar_diccionario_encriptado, cargar_diccionario, esta_en_diccionario
from permutacion import obtener_permutaciones

VOCALES_MINUSCULAS = "aeiou"
VOCALES_MAYUSCULAS = "AEIOU"


def construir_diccionario_sustitucion(permutacion_vocales):
    """

    Genera un diccionario donde, de acuerdo permutacion_vocales, las claves son las letras del
    mensaje original y los valores son los valores encriptados de cada letra.
    Solo deben sustituirse las vocales de acuerdo a permutacion_vocales, las consonantes no deben
    ser sustituidas.

    :param permutacion_vocales: Cadena de caracteres, con una permutación de vocales. El orden de las
    vocales en la permutacion define la sustitucion de vocales en el diccionario resultante.
    :return: Diccionario, con claves para letras mayusculas y minusculas.
    """

    lista_letras = string.ascii_lowercase
    diccionario_sustitucion = {}

    for letra_original in lista_letras:
        if letra_original in VOCALES_MINUSCULAS:
            letra_sustituta = permutacion_vocales[VOCALES_MINUSCULAS.index(letra_original)]
        else:
            letra_sustituta = letra_original

        diccionario_sustitucion[letra_original] = letra_sustituta
        diccionario_sustitucion[letra_original.upper()] = letra_sustituta.upper()

    return diccionario_sustitucion


class CodificadorPorSustitucion(object):

    def __init__(self, texto_mensaje, permutacion_vocales):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param permutacion_vocales: Cadena de caracteres, con la permutacion de vocales para el cifrado por sustitucion.
        """
        self.texto_mensaje = texto_mensaje
        self.diccionario_sustitucion = construir_diccionario_sustitucion(permutacion_vocales)
        self.mensaje_encriptado = aplicar_diccionario_encriptado(self.texto_mensaje, self.diccionario_sustitucion)

    def get_diccionario_sustitucion(self):
        """

        :return: Diccionario. Una copia del campo diccionario_sustitucion.
        """
        return dict(self.diccionario_sustitucion)

    def get_texto_mensaje(self):
        """
          :return: Cadena de caracteres. El valor del campo texto_mensaje.
          """
        return self.texto_mensaje

    def get_mensaje_encriptado(self):
        """
        :return: Cadena de caracteres. El valor del campo mensaje_encriptado.
        """
        return self.mensaje_encriptado


class DecodificadorPorSustitucion(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: Cadena de caracteres, con el mensaje a desencriptar.
        """
        self.mensaje_encriptado = mensaje_encriptado
        self.diccionario = cargar_diccionario("diccionario.txt")

    def descifrar_mensaje(self):
        """

        Desencripta mensajes codificados usando Cifrado por Sustitución. Para esto se realiza lo siguiente:
        - Probamos con todas las permutaciones de 5 vocales.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos la permutacion que genere el maximo numero de palabras en diccionario.txt.

        :return: Una cadena de caracteres con el mensaje decodificado.
        """

        palabras_en_diccionario = None
        mensaje_descifrado = self.mensaje_encriptado

        candidatos = obtener_permutaciones(VOCALES_MINUSCULAS)
        for candidato_permutacion in candidatos:
            candidato_descifrado = ""
            for letra in self.mensaje_encriptado:
                if letra in VOCALES_MINUSCULAS:
                    candidato_descifrado += VOCALES_MINUSCULAS[candidato_permutacion.index(letra)]
                elif letra in VOCALES_MAYUSCULAS:
                    candidato_descifrado += VOCALES_MAYUSCULAS[candidato_permutacion.index(letra)]
                else:
                    candidato_descifrado += letra

            palabras_candidato = candidato_descifrado.split()
            palabras_diccionario_candidato = 0
            for palabra in palabras_candidato:
                if esta_en_diccionario(self.diccionario, palabra):
                    palabras_diccionario_candidato += 1

            if palabras_en_diccionario is None or palabras_diccionario_candidato > palabras_en_diccionario:
                palabras_en_diccionario = palabras_diccionario_candidato
                mensaje_descifrado = candidato_descifrado

        return mensaje_descifrado

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        return list(self.diccionario)


if __name__ == "__main__":
    codificador = CodificadorPorSustitucion("Buenos dias, querido profesor!", "eaiuo")
    print(codificador.get_texto_mensaje())
    print(codificador.get_mensaje_encriptado())

    decodificador = DecodificadorPorSustitucion("Boanus dies, qoaridu prufasur!")
    print(decodificador.descifrar_mensaje())
