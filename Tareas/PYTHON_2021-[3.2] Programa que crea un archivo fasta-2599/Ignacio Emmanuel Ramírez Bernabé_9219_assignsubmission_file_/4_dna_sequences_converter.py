"""

NAME
        4_dna_sequences_converter.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/edit/master/python_scripts/4_dna_sequences_converter.py

DESCRIPTION
        This program creates a fasta file from the 4_dna_sequences.txt file

CATEGORY
        FASTA

USAGE
        python 4_dna_sequences_converter.py

ARGUMENTS
        No command line arguments

EXAMPLES
        Example: Run the program in the same directory as the 4_dna.sequences.txt file

        Usage: $ python 4_dna_sequences_converter.py

        Input:
        4_dna_sequences.txt

        Output:
        dna_sequences.fasta


"""
# Guardar direccion del archivo 4_dna_sequences.txt
file_path = "4_dna_sequences.txt"

# Abrir archivo
input_file = open(file_path)

# Crear/abrir el archivo donde se guardara el output en el modo de escritura
output_file = open("dna_sequences.fasta", "w")

# Leer cada una de las lineas de input_file
for line in input_file:
    # Cortar el primer elemento de la linea antes de un espacio
    header = line.split(' ')[0]
    # Cortar el segundo elemento de la linea despues del caracter "
    seq = line.split('\"')[1]
    # Eliminar los caracteres '-' de la secuencia
    seq = seq.replace('-', '')
    # Escribir el encabezado y la secuencia en el archivo fasta
    output_file.write(f"> {header}\n{seq.upper()}\n")

# Cerrar los archivos 4_dna_sequences.txt y dna_sequences.fasta
input_file.close()
output_file.close()
