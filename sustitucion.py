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

    return {}


class CodificadorPorSustitucion(object):

    def __init__(self, texto_mensaje, permutacion_vocales):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param permutacion_vocales: Cadena de caracteres, con la permutacion de vocales para el cifrado por sustitucion.
        """
        pass

    def get_diccionario_sustitucion(self):
        """

        :return: Diccionario. Una copia del campo diccionario_sustitucion.
        """
        return {}

    def get_texto_mensaje(self):
        """
          :return: Cadena de caracteres. El valor del campo texto_mensaje.
          """
        return ""

    def get_mensaje_encriptado(self):
        """
        :return: Cadena de caracteres. El valor del campo mensaje_encriptado.
        """
        return ""


class DecodificadorPorSustitucion(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: Cadena de caracteres, con el mensaje a desencriptar.
        """
        pass

    def descifrar_mensaje(self):
        """

        Desencripta mensajes codificados usando Cifrado por Sustitución. Para esto se realiza lo siguiente:
        - Probamos con todas las permutaciones de 5 vocales.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos la permutacion que genere el maximo numero de palabras en diccionario.txt.

        :return: Una cadena de caracteres con el mensaje decodificado.
        """

        return ""

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        return []


if __name__ == "__main__":
    codificador = CodificadorPorSustitucion("Buenos dias, querido profesor!", "eaiuo")
    print(codificador.get_texto_mensaje())
    print(codificador.get_mensaje_encriptado())

    decodificador = DecodificadorPorSustitucion("Boanus dies, qoaridu prufasur!")
    print(decodificador.descifrar_mensaje())
