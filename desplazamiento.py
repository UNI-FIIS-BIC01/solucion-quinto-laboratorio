import string

# INICIO: Codigo de soporte
import unicodedata


def remover_acentos(palabra_con_acentos):
    return ''.join(letra for letra in unicodedata.normalize('NFD', palabra_con_acentos)
                   if unicodedata.category(letra) != 'Mn')


def cargar_diccionario(nombre_archivo):
    """
    :param nombre_archivo: Archivo de texto.
    :return: Una lista de cadena de caracteres, conteniendo las palabras en el archivo
    nombre_archivo.
    """
    print("Cargando diccionario desde archivo...")
    with open(nombre_archivo, 'r', encoding='utf8') as archivo_diccionario:
        lineas = archivo_diccionario.readlines()

    diccionario = [remover_acentos(linea.strip().lower()) for linea in lineas]
    print("  ", len(diccionario), "palabras en diccionario.")
    return diccionario


def esta_en_diccionario(diccionario, palabra):
    """
    Verifica si palabra esta en diccionario, excluyendo espacios en blanco y signos
    de puntuacion.
    :param diccionario: Listado de cadenas de caracteres.
    :param palabra: Cadena de caracteres a verificar.
    :return: True si palabra esta en diccionario. False caso contrario.
    """
    palabra = palabra.lower()
    palabra = palabra.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return palabra in diccionario


def obtener_mensaje_confidencial():
    """
    :return: El contenido del archivo confidencial.txt, como cadena de caracteres.
    """
    archivo = open("confidencial.txt", "r")
    mensaje_confidencial = str(archivo.read())
    archivo.close()
    return mensaje_confidencial


# FIN: Codigo de soporte.

def construir_diccionario_desplazamiento(desplazamiento):
    """
    Genera un diccionario donde, de acuerdo al desplazamiento, las claves son las letras del
    mensaje original y los valores son los valores encriptados de cada letra.

    :param desplazamiento: Numero entero para el desplazamiento.
    :return: Diccionario, con claves para letras mayusculas y minusculas.
    """

    return {}


def aplicar_diccionario_encriptado(texto_mensaje, diccionario_encriptado):
    """

    :param texto_mensaje: Cadena de caracteres a encriptar.
    :param diccionario_encriptado: Diccionario para la encriptacion. Las claves son las letras
    original es y los valores las letras encriptadas.
    :return: La cadena texto_mensaje encriptada.
    """
    return ""


class CodificadorPorDesplazamiento(object):

    def __init__(self, texto_mensaje, desplazamiento):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param desplazamiento: Entero. El desplazamiento para el cifrado Cesar.
        """
        pass

    def get_desplazamiento(self):
        """
        :return: Entero. El valor del campo desplazamiento
        """
        return 0

    def get_diccionario_desplazamiento(self):
        """
        :return: Diccionario. Una copia del campo diccionario_desplazamiento.
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

    def cambiar_desplazamiento(self, nuevo_desplazamiento):
        """
        Permite actualizar el valor del desplazamiento usado para el Cifrado Cesar.
        :param nuevo_desplazamiento: Nuevo valor del desplazamiento.
        :return: None
        """
        pass


class DecodificadorPorDesplazamiento(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: Cadena de caracteres, con el mensaje a desencriptar.
        """
        pass

    def descifrar_mensaje(self):
        """
        Desencripta mensajes codificados usando el Codigo Cesar. Para esto se realiza lo siguiente:
        - Probamos con 26 valores de desplazamiento.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos el valor de desplazamiento que genere el maximo numero de palabras en diccionario.txt.

        :return: Tupla. El primer elemento es el mejor desplazamiento encontrado, y el segundo elemento es el mensaje
        desencriptado.
        """

        return 0, ""

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        return []


if __name__ == "__main__":
    mensaje_en_clave = DecodificadorPorDesplazamiento(obtener_mensaje_confidencial())
    print(mensaje_en_clave.descifrar_mensaje())
