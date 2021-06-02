"""
NAME 
  tarea7AT-errores.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
  calcula el porcentaje de AT de las secuencias de un archivo desde terminal

CATEGORY
  analisis de secuencia

USAGE
  tarea7AT-errores.py -i docs/4-Listas_y_loops/4_dna_sequences.txt -o -r 

ARGUMENTS
  -i    archivo de origen 
  -o    archivo de salida
  -r    decimales a mostrar
    
INPUT
    el archivo de origen se determina por argumentos
    el fomrato es el siguiente determinado por ejemplos:
    seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    seq_2 = "actgatcgacgatcgatcgatcacgact"
    seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"
    seq_4 = "acgtnnnnnacgtagctnnnnn"
    la secuencia se delimita por las comillas
OUTPUT
    el archivo de salida se determina por
    formato de salida determinado por ejemplos:
    AT content for seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    is 0.5
    AT content for seq_2 = "actgatcgacgatcgatcgatcacgact"
    is 0.5
    AT content for seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"
    is 0.4482758620689655
    skipping invalid sequence Sequence contains 10 N's


GITHUB
    https://github.com/psicilia/python_Class/blob/6f1166ebc9d14b36ffa1c4a7aab627a3dd957d39/src/tarea7AT-errores.py

"""

import argparse
from os import error, replace

# Create the parser
parser = argparse.ArgumentParser(description="Script que calcula el contenido de AT de un archivo desde linea de comandos")
# Argumentos
parser.add_argument("-i", "--input",
    #archivo de entrada, necesario
    metavar="path/to/file",
    help="direccion del archivo con secuencias de DNA",
    required=True
)
parser.add_argument("-o", "--output", nargs='?', const="not output file" ,
    #archivo de salida, no necesario
    help="Direccion del archivo de salida /n al no definr el output se mostrara en terminal",
     required=True
)
parser.add_argument("-r", "--round", nargs='?', const=2, 
    #numeros despues del punto decimal, no necesario
    help="Numero de digitos al redondear /n al no definir se asume 2",
    type=int,
     required=True
)
# Execute the parse_args() method
args = parser.parse_args()

class AmbiguousBaseError(Exception):
    pass

def get_at_content(dna):
    #determinamos el porcentaje de AT de la cadena dna
    dna = dna.upper()
    dna = dna.split('"')[1]
    #delimitamos con base en el formato del archivo
    if dna.count("N") > 0:
        raise AmbiguousBaseError(f'Sequence contains {dna.count("N")} N\'s')
        #si algun caracter es no determinado "N" saltamos la cadena
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    #calculamos el AT con base en las cuentas
    return round(at_content, args.round)
    #regresamos el valor redondeado con base en el parametro -r

# Abir archivo de lectura
try:
    file = open(args.input)
except IOError:

    print('error, ingresa nuevamente el nombre del archivo de entrada')
    args.input = input()
    try:
        file = open(args.input)
    except IOError:
        print('error al ingresar datos')
        pass
else:

    try:
        all_lines = file.readlines()
        file.close()
        # Leer todas las lineas y guardarlas en una lista
        if args.output != "not output file":
            fileW = open(args.output, "w")
            for seq in all_lines:
                try:
                    fileW.write('AT content for '+ seq +' is ' + str(get_at_content(seq)) + '\n' )
                except AmbiguousBaseError as ex:
                    fileW.write('skipping invalid sequence '+ ex.args[0] + '\n')         
        else:
            print('no hay archivo de salida, output a terminal')
            for seq in all_lines:
                try:
                    print('AT content for ' + seq + ' is ' + str(get_at_content(seq)))
                except AmbiguousBaseError as ex:
                    print('skipping invalid sequence '+ ex.args[0])
    except IOError:
        print('no se puede abrir el archivo de lectura')

