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
    :return: Diccionario, con claves para mayusculas y minusculas.
    """
    lista_letras = string.ascii_lowercase
    diccionario_desplazamiento = {}

    for indice in range(len(lista_letras)):
        indice_desplazado = indice + desplazamiento
        if indice_desplazado < len(lista_letras):
            letra_desplazada = lista_letras[indice_desplazado]
        else:
            letra_desplazada = lista_letras[indice_desplazado - len(lista_letras)]

        letra_original = lista_letras[indice]
        diccionario_desplazamiento[letra_original] = letra_desplazada
        diccionario_desplazamiento[letra_original.upper()] = letra_desplazada.upper()

    return diccionario_desplazamiento


def aplicar_diccionario_encriptado(texto_mensaje, diccionario_encriptado):
    """

    :param texto_mensaje: Cadena de caracteres a encriptar.
    :param diccionario_encriptado: Diccionario para la encriptacion. Las claves son las letras
    original es y los valores las letras encriptadas.
    :return: La cadena texto_mensaje encriptada.
    """
    mensaje_encriptado = ""
    for letra in texto_mensaje:
        if letra in diccionario_encriptado.keys():
            mensaje_encriptado += diccionario_encriptado[letra]
        else:
            mensaje_encriptado += letra

    return mensaje_encriptado


class CodificadorPorDesplazamiento(object):

    def __init__(self, texto_mensaje, desplazamiento):
        """

        :param texto_mensaje: Cadena de caracteres, con el mensaje a encriptar.
        :param desplazamiento: Entero. El desplazamiento para el cifrado Cesar.
        """
        self.texto_mensaje = texto_mensaje
        self.desplazamiento = desplazamiento
        self.diccionario_desplazamiento = {}
        self.mensaje_encriptado = ""
        self.cambiar_desplazamiento(desplazamiento)

    def get_desplazamiento(self):
        """
        :return: Entero. El valor del campo desplazamiento
        """
        return self.desplazamiento

    def get_diccionario_desplazamiento(self):
        """
        :return: Diccionario. Una copia del campo diccionario_desplazamiento.
        """
        return dict(self.diccionario_desplazamiento)

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

    def cambiar_desplazamiento(self, nuevo_desplazamiento):
        """
        Permite actualizar el valor del desplazamiento usado para el Cifrado Cesar.
        :param nuevo_desplazamiento: Nuevo valor del desplazamiento.
        :return: None
        """
        self.desplazamiento = nuevo_desplazamiento
        self.diccionario_desplazamiento = construir_diccionario_desplazamiento(nuevo_desplazamiento)
        self.mensaje_encriptado = aplicar_diccionario_encriptado(self.texto_mensaje, self.diccionario_desplazamiento)


class DecodificadorPorDesplazamiento(object):

    def __init__(self, mensaje_encriptado):
        """
        :param mensaje_encriptado: El mensaje a desencriptar.
        """
        self.mensaje_encriptado = mensaje_encriptado
        self.diccionario = cargar_diccionario("diccionario.txt")

    def descifrar_mensaje(self):
        """
        Desencripta mensajes codificados usando el Codigo Cesar. Para esto se realiza lo siguiente:
        - Probamos con 26 valores de desplazamiento.
        - Por cada valor, desencriptamos y contamos cuantas palabras estan en diccionario.txt.
        - Utilizamos el valor de desplazamiento que genere el maximo numero de palabras en diccionario.txt.

        :return: Tupla. El primer elemento es el mejor desplazamiento encontrado, y el segundo elemento es el mensaje
        desencriptado.
        """
        desplazamiento = None
        palabras_en_diccionario = None
        mensaje_descifrado = self.mensaje_encriptado

        for candidato_desplazamiento in range(26):
            desplazamiento_descifrado = 26 - candidato_desplazamiento
            diccionario_encriptado = construir_diccionario_desplazamiento(desplazamiento_descifrado)
            candidato_descifrado = aplicar_diccionario_encriptado(self.mensaje_encriptado, diccionario_encriptado)

            palabras_candidato = candidato_descifrado.split()
            palabras_diccionario_candidato = 0
            for palabra in palabras_candidato:
                if esta_en_diccionario(self.diccionario, palabra):
                    palabras_diccionario_candidato += 1

            if desplazamiento is None or palabras_diccionario_candidato > palabras_en_diccionario:
                desplazamiento = candidato_desplazamiento
                palabras_en_diccionario = palabras_diccionario_candidato
                mensaje_descifrado = candidato_descifrado

        return desplazamiento, mensaje_descifrado

    def get_diccionario(self):
        """
        :return: Una copia del campo diccionario.
        """
        return list(self.diccionario)


if __name__ == "__main__":
    # mensaje_en_clave = DecodificadorPorDesplazamiento(obtener_mensaje_confidencial())
    # print(mensaje_en_clave.descifrar_mensaje())

    decodificador = DecodificadorPorDesplazamiento("Xkxc gn Rgtw!")
    print(decodificador.descifrar_mensaje())  # En consola: (2, 'Viva el Peru!')
