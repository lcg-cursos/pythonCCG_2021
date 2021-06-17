import argparse
import re


"""

NAME
        9_at_regions.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/9_at_regions.py

DESCRIPTION
        This program finds the AT-rich regions of a sequence

CATEGORY
        DNA
        AT-rich regions

USAGE
        python 9_at_regions.py [OPTIONS]

ARGUMENTS
        -h, --help          show this help message and exit
        -i, --input         sequence

EXAMPLES
        Example 1: Run the program and give the dna sequence as input

        Usage: $ python 9_at_regions.py -i sequence

        Input:
        CTGCATTATATCGTACGAAATTATACGCGCG

        Output:
        An AT-rich region was found at position 4: ATTATAT
        An AT-rich region was found at position 17: AAATTATA


"""

# Crear la descripcion del programa
parser = argparse.ArgumentParser(description="Script that finds the AT-rich regions of a sequence")

# Anadir los argumentos
parser.add_argument("-i", "--input",
                    metavar="sequence",
                    help="DNA sequence")


# Crear la excepcion AmbiguousBaseError
class AmbiguousBaseError(Exception):
    pass


# Revisar si la secuencia es valida
def check_seq(seq):
    # Dar un error si la secuencia no es de DNA
    if not re.search(r'[ATGC]', seq):
        raise AmbiguousBaseError("Invalid sequence: No bases found")

    # Dar un error si la secuencia de DNA contiene caracteres invalidos
    invalid_bases = re.findall(r'[^ATGC]', seq)
    if invalid_bases:
        raise AmbiguousBaseError(f'Ambiguous bases found: {invalid_bases}')


# Ejecutar el metodo parse_args()
args = parser.parse_args()

# Obtener regiones ricas en AT
try:
    # Revisar si la secuencia es valida
    dna = args.input
    check_seq(dna)

    # Buscar regiones ricas en AT
    if re.search(r'[AT]{5,}', dna):
        at_regions = re.finditer(r'[AT]{5,}', dna)
        for region in at_regions:
            base = region.group()
            pos = region.start()
            print("An AT-rich region was found at position " + str(pos) + ": " + base)
    else:
        print("No AT-rich regions were found")

# Imprimir un error si la secuencia no es valida
except AmbiguousBaseError as ex:
    print(ex)
