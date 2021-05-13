'''
NAME
       [fasta_sequences].py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>

DESCRIPTION
        [Este programa recibe como input un archivo .txt con secuencias de nucleótidos y con ellas crea un archivo .fasta]

CATEGORY
       [Genomic sequence.]

USAGE
       [De uso bioinformático. Corre en python.
       Este script corre desde el directorio src
       El archivo .txt del que se leen las secuencias está ubicado en la ruta python_class/docs/4_dna_sequences.txt
       El archivo .fasta se generará en el directorio src]

OPTIONS
       [Este programa no tiene opciones.]

EXAMPLES
       [Input: 4_dna_sequences.txt: seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
                                    seq_2 = "actgatcgacgatcgatcgatcacgact"
                                    seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"
        Output: dna_sequences.fasta: > seq_1
                                    ATCGTACGATCGATCGATCGCTAGACGTATCG
                                    > seq_2
                                    ACTGATCGACGATCGATCGATCACGACT
                                    > seq_3
                                    ACTGACACTGTACTGTACATGTG          ]

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/fasta_sequences.py]

'''

# Abrir el archivo que contiene las secuencias.
file = open("data/4_dna_sequences.txt")

# Leer todas las lineas y guardarlas en una lista
all_lines = file.readlines()

# Cerrar el archivo.
file.close()

# Inicializar un contador.
n = 1

# Crear el archivo en el que se guardará el output, estará en el directorio docs, dentro del repositorio.
new_file = open("output/dna_sequences.fasta", "w")

# Procesar cade línea del archivo input y escribir el archivo output.
for line in all_lines:
    line = line.split((" ")) # Divide cada línea por ""
    line = (line [-1]) # Quedarnos con el último elemento
    line = line.replace('-', '') # Cambiar - por nada
    line = line.replace('"', '') # Cambiar " por nada
    line = line.upper() # Hacer todas las secuencias en letras mayúsculas
    line = ("> seq_" + str(n) + "\n" + line) # Agregar el formato restante de un archivo .fasta
    n += 1
    print(line) # Imprimir el archivo
    new_file.write(line) # Escribir el nuevo archivo .fasta

# Cerrar el nuevo archivo.
new_file.close()


