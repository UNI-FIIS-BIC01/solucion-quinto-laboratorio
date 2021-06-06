def obtener_permutaciones(cadena):
    """
    Genera todas las permutaciones diferentes para una cadena de caracteres,
    de manera RECURSIVA.

    :param cadena:Una cadena de caracteres. Puede tener caracteres repetidos.
    :return: Una lista de cadena de caracteres diferentes. Contiene TODAS las permutaciones
    DIFERENTES de la cadena pasada como parametro.
    """
    if len(cadena) == 1:
        return [cadena]
    else:
        lista_permutaciones = []
        primer_caracter = cadena[0]
        resto_cadena = cadena[1:]

        permutaciones_resto = obtener_permutaciones(resto_cadena)
        for permutacion in permutaciones_resto:
            for indice in range(len(permutacion) + 1):
                if indice < len(permutacion):
                    nueva_permutacion = permutacion[0: indice] + primer_caracter + permutacion[indice:]
                else:
                    nueva_permutacion = permutacion + primer_caracter

                if nueva_permutacion not in lista_permutaciones:
                    lista_permutaciones.append(nueva_permutacion)

        return lista_permutaciones


if __name__ == "__main__":
    print(obtener_permutaciones("abcb"))
