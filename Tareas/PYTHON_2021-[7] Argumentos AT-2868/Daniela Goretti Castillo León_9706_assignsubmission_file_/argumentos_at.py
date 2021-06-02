'''
NAME
    argumentos_at.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa toma argumentos dados por la línea de comandos, pidiendo un archivo con secuencias de DNA. Evalúa si
    las líneas o secuencias contienen N's en su nombre, si se pasaron los argumentos correctos y si el directorio es
    válido con ayuda del manejo de errores.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    argumentos_at.py -i <Archivo input> [argumentos opcionales]

ARGUMENTS
    -i, --input     Pide un archivo de texto con secuencias de DNA (argumento necesario).
    -o, --output    Pide un archivo output con los resultados del archivo (argumento opcional).
    -r, --round     Pide los dígitos a los que se quiere redondear el contenido de AT (argumento opcional).

PACKAGES
    os          Este paquete ayuda a definir si un archivo se encuentra o no dentro del directorio mandado.
    sys         El paquete sys cierra el directorio escrito por el usuario.
    argparse    El paquete argparse ayuda a definir los argumentos escritos en el programa.

INPUT
     4_dna_sequences.txt (archivo que contiene las secuencias de DNA)

OUTPUT
    Archivo con contenido de AT de secuencias (opcional)

EXAMPLES
    Example 1: Se tiene el archivo 4_dna_sequences.txt, el cual cuenta con 3 secuencias distintas de DNA (el cual se
    encuentra en el directorio ../docs/4_dna_sequences.txt). Las líneas de este archivo contienen guiones y letras en
    minúsculas. Se coloca este archivo con ayuda del argumento -i o --input, de manera que éste se modifica (se quitan
    los guiones y se convierte la secuencia a mayúsculas), y entra a una función que calcula el contenido de AT de las
    secuencias. En esta función primero se pregunta si existen "N's" en la secuencia de DNA, y en dado caso de que así
    sea entonces se imprime el número de N's que se tienen e invoca un error. Si este no es el caso entonces se continúa
    a hacer la función, dando el contenido de AT de la secuencia gracias a los decimales que hayamos indicado o el valor
    default (que son dos decimales). Estas condiciones suceden si y sólo si el archivo contiene el directorio indicado,
    si no entonces se imprime un error.
    En este ejemplo no se contienen N's, por lo que las tres secuencias muestran resultados de contenidos de AT. Si se
    quiere, se pueden cambiar los valores de redondeo de decimales de estos contenidos o se puede dar un archivo dónde
    guardar estos resultados con ayuda de los argumentos opcionales -r o --round y -o o --output, respectivamente.

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/argumentos_at.py

'''

# 1. Importar librerías
import argparse
import os
import sys

# 2. Crear Parser
parser = argparse.ArgumentParser(description="Script que calcula el contenido de AT con uso de argumentos desde la"
                                             "línea de comandos")

# Agregar argumentos necesarios y opcionales
parser.add_argument("-i", "--input", metavar="Path for file", help="Archivo con secuencias de ADN", required=True)
parser.add_argument("-o", "--output", help="Archivo output con resultados de contenido de AT", required=False)
parser.add_argument("-r", "--round", help="Dígitos de redondeo de contenido de AT", required=False)

# 3. Escribir función get_at_content


def get_at_content(dna, decimales=2):
    if dna.count("N") > 0:
        raise ValueError("Sequence contains" + int(dna.count("N")) + "N\'s")
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return round(at_content, decimales)


# 4. Ejecutar métodos
args = parser.parse_args()
input_path = args.Path
if not os.path.isdir:
    print("Línea inválida: argumentos faltantes")
    sys.exit()

# 5. Llamar a función, corregir secuencias
file = open(input_path)
try:
    all_lines = file.readlines()
    file.close()
    new_file = open("dna_sequences.fasta", "w")
    for line in all_lines:
        line = line.replace("-", "")
        line = line.replace('"', '')
        sequences = line.split(" = ")
        name = sequences[0]
        nucleotides = str(sequences[1]).upper()
        dna_input = name + nucleotides
        new_file.write(get_at_content(dna_input))

except IOError as ex:
    print("Directorio inválido: no se encontró el archivo")
