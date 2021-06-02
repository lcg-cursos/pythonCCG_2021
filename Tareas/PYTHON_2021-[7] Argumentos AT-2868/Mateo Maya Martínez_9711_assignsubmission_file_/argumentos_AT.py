'''
NAME
       [argumentos_AT].py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>

DESCRIPTION
        [Este programa calcula el contenido de AT de ciertas secuencias que se encuentra en un archivo .txt usando comandos en terminal.]

CATEGORY
       [Sequence.]

USAGE
       [De uso bioinformático. Corre en python.]

OPTIONS
       [ -h, --help     Muestra la ayuda del script

        -i, --input     Es el archivo del que se leeran las secuencias.

        -o, --output    Archivo en el que se guardarán los porcentajes ]

EXAMPLES
       [Input file: 4_dna_sequence.txt
        Output: Archivo .txt con los porcentajes]

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/argumentos_AT.py]
'''

#Importar la librería para escribir los argumentos desde terminal.
import argparse

#Definir el parser.
parser = argparse.ArgumentParser(description= "Este programa calcula el porcentaje de AT de una serie de secuencias encontradas en un archivo" )

#Definir los argumentos del programa.
parser.add_argument("-i", "--input",
                    help="Archivo con las secuencias",
                    required=True)

parser.add_argument("-o", "--output",
                    help="Archivo en el que se guardarán los porcentajes",
                    default="contenido_AT_out.txt", required=False)

#Ejecutar el método parse_args
args = parser.parse_args()

#Función que calcula el contenido de AT
def get_AT_content (sequence, decimales=2):

    sequence = sequence.upper()
    if sequence.count("N") > 0:
        raise ValueError(f'Your sequence has {sequence.count("N")} N´s')
    A = sequence.count("A")
    T = sequence.count("T")
    length = len(sequence)
    AT_percentage = (A + T)/length
    return round (AT_percentage, decimales)

#Abrir el archivo que se pase por línea de comandos
try:
    file = open(args.input)
#Si no se encuentra el archivo imprimir un mensaje y solicitar un archivo válido.
except IOError as ex:
    print ("Couldn´t find the file. " + ex.strerror)
    new_file = input("Please enter a valid file: \n")
    file = open (new_file)

#Leer el archivo línea por línea y cerrarlo
finally:
    all_lines = file.readlines()
    file.close()

#Crear el archivo de salida.
output_file = open(args.output, "w")

#i será un iterador que nos ayudará con el formato del archivo output.
i = 0

#Dar el formato que necesitamos a cada línea del archivo autput.
for line in all_lines:
    line = line.split(" = ")
    sequence = line[1]
    sequence = str(sequence).replace('"', "")
    sequence = str(sequence).replace("-", "")
    i+=1

#Escribimos el archivo output
    try:
        output_file.write("Seq" + str(i) + " has " + str(get_AT_content(sequence)) + "% AT content \n")
#Si las secuencias en el archivo input tienen un error, se muestra el error en pantalla y no se agregan al archivo output.
    except ValueError as ex:
        print ("Skipping sequence " + str(i)+ ". " + ex.args[0])

#Cerrar el archivo output
output_file.close
