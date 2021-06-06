# BIC01: Quinto Laboratorio

## Primera Parte

Complete la implementación de la función `obtener_permutaciones(cadena)`. Esta función toma como entrada una cadena de
caracteres, y genera una lista con todas las [permutaciones](https://es.wikipedia.org/wiki/Permutaci%C3%B3n) **
diferentes** de las letras de dicha cadena de caracteres.

La función `obtener_permutaciones(cadena)` es una función **recursiva**. La intuición respecto al algoritmo es la
siguiente:

* Si `cadena` tiene un solo carácter, `obtener_permutaciones(cadena)` produce una lista con un solo elemento: `cadena`.

* Si `cadena` tiene más de un carácter, `obtener_permutaciones(cadena)` puede obtenerse de la siguiente manera:
    1. Divide cadena en dos partes: La primera letra, y el resto. Por ejemplo, si cadena es `abcd`, podemos dividirla
       en `a` y `bcd`.
    2. Obtenemos las permutaciones de la segunda parte (`bcd`), y generamos nuevas permutaciones colocando la primera
       parte (`a`)  en distintas posiciones **por cada permutación**. Por ejemplo, dado que las permutaciones de `bcd`
       son `['bcd', 'cbd', 'cdb', 'bdc', 'dbc', 'dcb']`:
        * Con `bcd`, podemos generar `['abcd', 'bacd', 'bcad', 'bcda']`
        * Con `cbd`, podemos generar `['acbd', 'cabd', 'cbad', 'cbda']`
        * Y asi sucesivamente.

Realice la implementación en el archivo `permutacion.py`. A modo de ejemplo, al
invocar `print(obtener_permutaciones("abcb"))` tendría el siguiente resultado en consola:

```commandline
['abcb', 'bacb', 'bcab', 'bcba', 'acbb', 'cabb', 'cbab', 'cbba', 'abbc', 'babc', 'bbac', 'bbca']
```

## Segunda Parte

Implemente un programa para encriptar y desencriptar mensajes usando el
[Código de César (o cifrado por desplazamiento)](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar). Para esto, debe
realizar lo siguiente:

* Complete la implementación de la función `construir_diccionario_desplazamiento(desplazamiento)`. Esta función toma
  como parámetro el valor entero `desplazamiento` y produce como resultado un diccionario. En este diccionario, las
  claves son letras y los valores las letras encriptadas. Este diccionario debe contar con claves para todas las letras
  del [alfabeto inglés](https://es.wikipedia.org/wiki/Alfabeto_ingl%C3%A9s), considerando mayúsculas y minúsculas.
  Además debe haber consistencia entre la encriptación de mayúsculas y minúsculas
  (si encriptamos `a` como `b`, `A` debe ser encriptada como `B`). Por ejemplo,
  ejecutar `print(construir_diccionario_desplazamiento(1))` deberia mostrar los siguiente en consola:

    ```commandline
    {'a': 'b', 'A': 'B', 'b': 'c', 'B': 'C', 'c': 'd', 'C': 'D', 'd': 'e', 'D': 'E', 'e': 'f', 'E': 'F', 'f': 'g', 'F': 'G', 'g': 'h', 'G': 'H', 'h': 'i', 'H': 'I', 'i': 'j', 'I': 'J', 'j': 'k', 'J': 'K', 'k': 'l', 'K': 'L', 'l': 'm', 'L': 'M', 'm': 'n', 'M': 'N', 'n': 'o', 'N': 'O', 'o': 'p', 'O': 'P', 'p': 'q', 'P': 'Q', 'q': 'r', 'Q': 'R', 'r': 's', 'R': 'S', 's': 't', 'S': 'T', 't': 'u', 'T': 'U', 'u': 'v', 'U': 'V', 'v': 'w', 'V': 'W', 'w': 'x', 'W': 'X', 'x': 'y', 'X': 'Y', 'y': 'z', 'Y': 'Z', 'z': 'a', 'Z': 'A'}
    ```
* Complete la implementación de la función `aplicar_diccionario_encriptado(texto_mensaje, diccionario_encriptado)`. Esta
  función toma como parámetros la cadena de caracteres que queremos encriptar `texto_mensaje` y el diccionario con
  letras y sus valores encriptados. Produce una cadena de caracteres con el valor encriptado de `texto_mensaje`. Por
  ejemplo:

    ```python
    diccionario_encriptado = construir_diccionario_desplazamiento(1)
    print(aplicar_diccionario_encriptado("Viva el Peru!", diccionario_encriptado )) ## En consola: Wjwb fm Qfsv!
    ```
* Complete la implementación de la clase `CodificadorPorDesplazamiento`, utilizada para codificar mensajes usando el
  Código de César. Esta clase tiene los siguientes atributos:
    1. El campo `texto_mensaje`: Una cadena de caracteres con el texto a encriptar.
    2. El campo `desplazamiento`: Un entero, con el desplazamiento para el cifrado Cesar.
    3. El campo `diccionario_desplazamiento`: Un diccionario, con las letras como claves y sus valores encriptados como
       valores. Utilizar `construir_diccionario_desplazamiento` para su generación.
    4. El campo `mensaje_encriptado`: Una cadena de caracteres con el valor encriptado de `texto_mensaje`.
       Utilizar `aplicar_diccionario_encriptado` para su generación.
    5. El método `get_desplazamiento`: Retorna el valor de `desplazamiento` utilizado para el encriptado.
    6. El método `get_diccionario_desplazamiento`: Retorna una **copia** del diccionario utilizado para el encriptado.
    7. El método `get_texto_mensaje`: Retorna el valor de `texto_mensaje`, que representa el mensaje a encriptar.
    8. El método `get_mensaje_encriptado`: Retorna el valor de `mensaje_encriptado`, que representa el mensaje
       encriptado.
    9. El método `cambiar_desplazamiento`: Permite actualizar el valor de `desplazamiento` utilizado para el cifrado. **
       Tenga presente el impacto de este método en el resto de atributos**.

  A modo de ejemplo:

    ```python
    codificador = CodificadorPorDesplazamiento("Viva el Peru!", 1)
    print(codificador.get_texto_mensaje()) # En consola: Viva el Peru!
    print(codificador.get_desplazamiento()) # En consola: 1
    print(codificador.get_mensaje_encriptado()) # En consola: Wjwb fm Qfsv!

    codificador.cambiar_desplazamiento(2)
    print(codificador.get_mensaje_encriptado()) # En consola: Xkxc gn Rgtw!
    ```
* Complete la implementación de la clase `DecodificadorPorDesplazamiento`, utilizada para decodificar mensajes
  encriptados mediante el Código de César. Esta clase tiene los siguientes atributos:
    1. El campo `mensaje_encriptado`: Una cadena de caracteres, con el mensaje a desencriptar.
    2. El campo `diccionario`: Una lista de cadenas de caracteres, donde cada elemento es una palabra válida del
       español. Utilizar `cargar_diccionario("diccionario.txt")` para su generación.
    3. El método `get_diccionario`: Retorna una **copia** del campo `diccionario`.
    4. El método `descifrar_mensaje`: Retorna una tupla con dos elementos. El primer elemento el desplazamiento
       utilizado durante el encriptado y el segundo es una cadena de caracteres con el mensaje descifrado. Para
       encontrar el desplazamiento, el algoritmo prueba los valores desde `0` hasta `26`. Por cada desplazamiento `d`,
       desencripta `mensaje_encriptado` (puede desplazar `26 -d`), y verifica cuantas palabras del mensaje desencriptado
       son palabras válidas en castellano (utilizar la función `esta_en_diccionario`). El desplazamiento a utilizar es
       el que genere **el máximo número de palabras válidas**.

  A modo de ejemplo:
    ```python
        decodificador = DecodificadorPorDesplazamiento("Xkxc gn Rgtw!")
        print(decodificador.descifrar_mensaje()) # En consola: (2, 'Viva el Peru!')
    ```
* Utilice `DecodificadorPorDesplazamiento` para desencriptar el mensaje almacenado en `confidencial.txt`. Puede leer el
  archivo usando la función `obtener_mensaje_confidencial`.

Implemente la segunda parte en el archivo `desplazamiento.py`.

## Tercera Parte

Implemente un programa para encriptar y desencriptar mensajes
usando [Cifrado por sustitución](https://es.wikipedia.org/wiki/Cifrado_por_sustituci%C3%B3n). Para esto, debe realizar
lo siguiente:

* Complete la implementación de la función `construir_diccionario_sustitucion(permutacion_vocales)`. Esta función toma
  como parámetro la cadena de caracteres `permutacion_vocales` y produce como resultado un diccionario. En este
  diccionario, las claves son letras y los valores las letras encriptadas. Este diccionario debe contar con claves para
  todas las letras del [alfabeto inglés](https://es.wikipedia.org/wiki/Alfabeto_ingl%C3%A9s), considerando mayúsculas y
  minúsculas. Además debe haber consistencia entre la encriptación de mayúsculas y minúsculas
  (si encriptamos `a` como `b`, `A` debe ser encriptada como `B`). En nuestra implementación, **sólo vamos a sustituir
  vocales, de acuerdo al orden de `permutacion_vocales`**. Si `permutacion_vocales` es `"eaiuo"`, entonces `"a"` debe
  ser sustituida por `"e"`, `"e"` debe ser sustituida por `"a"`,
  `"i"` no es sustituida, `"o"` debe ser sustituida por `"u"` y `"u"` debe ser sustituida por `"o"`. Las consonantes 
  **no** deben ser sustituidas. Entonces, al ejecutar `print(construir_diccionario_sustitucion("eaiuo"))` deberia mostrar
  los siguiente en consola:

    ```commandline
    {'a': 'e', 'A': 'E', 'b': 'b', 'B': 'B', 'c': 'c', 'C': 'C', 'd': 'd', 'D': 'D', 'e': 'a', 'E': 'A', 'f': 'f', 'F': 'F', 'g': 'g', 'G': 'G', 'h': 'h', 'H': 'H', 'i': 'i', 'I': 'I', 'j': 'j', 'J': 'J', 'k': 'k', 'K': 'K', 'l': 'l', 'L': 'L', 'm': 'm', 'M': 'M', 'n': 'n', 'N': 'N', 'o': 'u', 'O': 'U', 'p': 'p', 'P': 'P', 'q': 'q', 'Q': 'Q', 'r': 'r', 'R': 'R', 's': 's', 'S': 'S', 't': 't', 'T': 'T', 'u': 'o', 'U': 'O', 'v': 'v', 'V': 'V', 'w': 'w', 'W': 'W', 'x': 'x', 'X': 'X', 'y': 'y', 'Y': 'Y', 'z': 'z', 'Z': 'Z'}
    ```
* Complete la implementación de la clase `CodificadorPorSustitucion`, utilizada para codificar mensajes usando el
  Cifrado por Sustitución. Esta clase tiene los siguientes atributos:
    1. El campo `texto_mensaje`: Una cadena de caracteres con el texto a encriptar.
    2. El campo `diccionario_sustitucion`: Un diccionario, con las letras como claves y sus valores encriptados como
       valores. Utilizar `construir_diccionario_sustitucion` para su generación.
    4. El campo `mensaje_encriptado`: Una cadena de caracteres con el valor encriptado de `texto_mensaje`.
       Utilizar `aplicar_diccionario_encriptado`, implementada en la segunda parte, para su generación.
    6. El método `get_diccionario_sustitucion`: Retorna una **copia** del diccionario utilizado para el encriptado.
    7. El método `get_texto_mensaje`: Retorna el valor de `texto_mensaje`, que representa el mensaje a encriptar.
    8. El método `get_mensaje_encriptado`: Retorna el valor de `mensaje_encriptado`, que representa el mensaje
       encriptado.

  A modo de ejemplo:

    ```python
    codificador = CodificadorPorSustitucion("Buenos dias, querido profesor!", "eaiuo")
    print(codificador.get_texto_mensaje()) # En consola: Buenos dias, querido profesor!
    print(codificador.get_mensaje_encriptado()) # En consola: Boanus dies, qoaridu prufasur!
  ```

* Complete la implementación de la clase `DecodificadorPorSustitucion`, utilizada para decodificar mensajes encriptados
  mediante Cifrado por Sustitución. Esta clase tiene los siguientes atributos:
    1. El campo `mensaje_encriptado`: Una cadena de caracteres, con el mensaje a desencriptar.
    2. El campo `diccionario`: Una lista de cadenas de caracteres, donde cada elemento es una palabra válida del
       español. Utilizar `cargar_diccionario("diccionario.txt")` para su generación.
    3. El método `get_diccionario`: Retorna una **copia** del campo `diccionario`.
    4. El método `descifrar_mensaje`: Retorna una cadena de caracteres con el mensaje descifrado. Para encontrar la
       permutación usada durante la encriptación, el algoritmo prueba con todas las permutaciones posibles para las
       cinco vocales, calculadas mediante `obtener_permutaciones` (primera parte). Por cada permutación, desencripta `mensaje_encriptado` , y verifica cuantas palabras del mensaje desencriptado
       son palabras válidas en castellano (utilizar la función `esta_en_diccionario`). El permutación a utilizar es la
       que genere **el máximo número de palabras válidas**.

  A modo de ejemplo:
    ```python
    decodificador = DecodificadorPorSustitucion("Boanus dies, qoaridu prufasur!")
    print(decodificador.descifrar_mensaje()) # En consola: Buenos dias, querido profesor!
    ```

Implemente la segunda parte en el archivo `sustitucion.py`.
