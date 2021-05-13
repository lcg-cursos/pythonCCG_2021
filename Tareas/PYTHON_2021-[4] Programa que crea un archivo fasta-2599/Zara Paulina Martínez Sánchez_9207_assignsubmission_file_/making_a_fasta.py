"""
## NAME
    making_a_fasta.py

## VERSION

    [0.0]

## AUTHOR

    Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

    05/05/2021

## DESCRIPTION

    Este programa crea un archivo fasta con base en la información del archivo dado

## CATEGORY

    Sequence analysis

## USAGE

    making_a_fasta.py utiliza el archivo 4_dna_sequences.txt ubicado en /python_class/data
    El archivo fasta se generará en el directorio src

## ARGUMENTS
    No hay argumentos

## EXAMPLES

    Input:
        4_dna_sequences.txt
    Output:
        Archivo file.fasta conla siguiente información:
        > seq_1
        ATCGTACGATCGATCGATCGCTAGACGTATCG
        > seq_2
        ACTGATCGACGATCGATCGATCACGACT
        > seq_3
        ACTGACACTGTACTGTACATGTG

## GITHUB LINK
    https://github.com/zara-ms/python_class/tree/master/src

"""
# Acceder al archivo a utilizar
file = open("../../Desktop/python_class/data/4_dna_sequences.txt")

# Generar una lista con las lineas del archivo
all_lines = file.readlines()

# Cerrar el archivo
file.close()

# Abrir el archivo file.fasta donde se va a escribir el resultado
archivo = open("file.fasta","w")

# For para todas las lineas
for line in all_lines:
#    Dividir la linea usando " = "
    line1 = line.split("=")
#    Guardar el nombre y la secuencia en variables diferentes
    name = line1[0]
    seq1 = line1[1]
#    Quitar las lineas "-" de la secuencia
    seq2 = (seq1.replace('-',''))
#    Quitar comillas de la secuencia
    seq3 = (seq2.replace('"',''))
#    Cambiar los nucleotidos a mayusculas
    seq4 = seq3.upper()
#    Escribir en el archivo en formato fasta
    archivo.write("> " + name + "\n" + seq4)

# Cerrar el archivo que se utilizó
archivo.close()
