'''
NAME
    at_riqueza.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa evalúa si una secuencia dada por el usuario tiene o no caracteres que no correspondan a bases
    nucleotídicas, si es así entonces imprime un error, y si no entonces evalúa si su contenido de AT es alto.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    at_riqueza.py [sin argumentos]

ARGUMENTS
    No se requieren argumentos para este programa

PACKAGES
    re      Ayuda a escribir expresiones regulares

FUNCTIONS
    contenido_at	Evalúa la secuencia dada por el usuario

INPUT
    Secuencia de ADN dada por el usuario

OUTPUT
    Imprime un mensaje de error si la secuencia contiene caracteres incorrectos (también los imprime).
        Se encontró uno o más caracteres no pertenecientes a bases nucleotídicas:
        <caracter incorrecto>  encontrada en posición  <ubicación de caracter incorrecto>

    Si los caracteres no son incorrectos, se imprimen diferentes mensajes dependiendo de si el contenido de AT es alto o
    no:
    Si es alto:
        Región rica en contenido de AT: ( <posición inicial>, <posición final> ), match:  <match>
    Si es bajo:
        No se encontraron regiones ricas en AT

EXAMPLES
    Example 1: Se tiene la secuencia CTGCATTATATCGTACGAAATTATACGCGCG. Esta secuencia contiene dos regiones con contenido
    de AT alto (con un fragmento de más de cinco bases de éstas). Al pasar por la función se revisa si se tienen
    caracteres incorrectos. Como en este caso no se tienen, entonces se procede a calcular si tiene o no regiones con un
    alto contenido de AT. Al ver que es así, entonces imprime las posiciones donde se encuentra el match y la secuencia
    del fragmento deseado:
        Región rica en contenido de AT: ( 4 , 11 ), match:  ATTATAT
        Región rica en contenido de AT: ( 17 , 25 ), match:  AAATTATA

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/at_riqueza.py

'''
# 1. Importar librería re.
import re

# 2. Definir error de excepción.


class AmbiguousBaseError (Exception):
    pass

# 3. Definir función que verifique la secuencia dada por el usuario.


def contenido_at(dna):
    """
    Verifica si la secuencia contiene una región con un contenido alto de AT. Después, evalúa si la secuencia contiene
    caracteres que no sean A, T, C o G (usa try y except para controlar estas acciones).
    :param dna: la secuencia dada por el usuario (a evaluar).
    :return: imprime si se tiene un caracter incorrecto (se muestra cuál es y en dónde está), imprime la región o
    regiones que tienen un contenido alto de AT (su posición y match) si se tienen, si no entonces se imprime que no se
    encontraron regiones ricas de estos nucleótidos.
    """
    try:
        if re.finditer(r"[ATCG]", dna):
            alto_at = re.finditer(r"[AT]{5,}", dna)
            if alto_at and re.finditer(r"[ATCG]", dna):
                for at in alto_at:
                    region = at.group()
                    start = at.start()
                    final = at.end()
                    print("Región rica en contenido de AT: (", start, ",", final, "), match: ", region)
        if re.finditer(r"[ATCG]", dna) and not re.search(r"[AT]{5,}", dna):
            print("No se encontraron regiones ricas en AT")
        if re.finditer(r"[^ATCG]", dna):
            raise AmbiguousBaseError

    except AmbiguousBaseError:
        matches = re.finditer(r"[^ATCG]", dna)
        for m in matches:
            if m:
                print("Se encontró uno o más caracteres no pertenecientes a bases nucleotídicas: ")
            base = m.group()
            pos = m.start()
            print(base, " encontrada en posición ", str(pos))


# 4. Pedir el input, guardar la secuencia y llamar a función contenido_at.
print("Escriba la secuencia de DNA: \n")
dna_input = input()
contenido_at(dna_input)
