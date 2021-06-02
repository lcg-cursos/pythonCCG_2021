"""
## NAME
        at_content_arguments.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

        26/05/2021

## DESCRIPTION

        Este programa recibe argumentos desde linea de comando, contiene manejo de errores
        y calcula el contenido de AT dando como output el archivo at_content.txt

## CATEGORY

        Sequence analysis

## USAGE

        at_content_arguments.py es de uso bioinformático

## ARGUMENTS

    -i,--input Ruta del archivo input la cual contiene secuencias de DNA
    -o,--output Ruta del archivo output con el contenido de AT de las secuencias

## EXAMPLES
    Input:
    $: python3 at_content_arguments.py -i 4_dna_sequences.txt -o at_content.txt

    Output:
    at_content.txt

## GITHUB LINK
        https://github.com/zara-ms/python_class/tree/master/src

"""
# Libreria a usar
import argparse

# Crear a parser
parser = argparse.ArgumentParser(description = "Este programa calcula el contenido de AT de secuencias en archivos")

# Añadir argumentos
parser.add_argument("-i", "--input",
                    metavar="Direccion del archivo a analizar",
                    type=str,
                    help="Archivo con la secuencia de DNA",
                    required=True)
# Argumento opcional
parser.add_argument("-o", "--output",
                    metavar="Ruta del archivo output",
                    type=str,
                    help="Archivo con el contenido de AT de la secuencia",
                    required=False)

# Ejecutar argumentos
args = parser.parse_args()
dir_input = args.input
dir_output = args.output

# Determinar el contenido de AT mediante una función
def get_at_content(dna):
#   Marcar error si la secuencia de DNA contiene Ns
    if dna.upper.count("N") > 0:
        raise ValueError(f'La secuencia contiene {dna.count("N")} N\'s')
    length = len(dna)
    a_count = dna.upper.count('A')
    t_count = dna.upper.count('T')
    at_content = (a_count + t_count) / length
    return round(at_content)

# Solicitar el input en caso de no encontrar el archivo
try:
    f = open(dir_input)
except IOError:
    print("Ingrese la direccion del archivo a analizar")
    dir_input = input()

# Lectura del input
file = open(dir_input)
all_lines = file.readlines()
file.close()

# Abrir el archivo donde se guardará el output
archivo_output = open("at_content.txt", "w")

# Modificar las lineas del archivo input
for lines in all_lines:
    sec1 = lines.split(" = ")
    sec2 = str(sec1[1]).replace('-', '')
    sec3 = sec2.replace('"', '')
    archivo_output.write(f'{sec1[0]} tiene un contenido de AT de {get_at_content(sec3)}')

archivo_output.close()
