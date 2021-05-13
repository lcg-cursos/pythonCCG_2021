'''
NAME
    Creacion_archivo_fasta.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa crea un archivo fasta a partir de un archivo con secuencias ya existente.

CATEGORY
    Archivos fasta

USAGE
    Creacion_archivo_fasta.py [sin opciones]

ARGUMENTS
    [sin argumentos]

INPUT
    4_dna_sequences.txt (archivo que contiene las secuencias de DNA)

OUTPUT
    dna_sequences.fasta (archivo de texto con formato fasta)


EXAMPLES
    Example 1: Se tiene el archivo 4_dna_sequences.txt con tres secuencias distintas. Estas secuencias se caracterizan
    por contener el nombre de la secuencia (seq_1, seq_2 o seq_3), un signo de "=" y la secuencia de DNA escrita entre
    comillas dobles. La secuencia número 2 está escrita con las bases en minúsculas, mientras que la número 3 contiene
    guiones que interrumpen la secuencia. Para convertir este archivo a otro de tipo fasta, primero se abre el archivo
    con las secuencias (4_dna_sequences.txt), después se leen esas líneas y se guardan en una variable conocida como
    file. Después se leen las líneas del archivo con el método .readlines() y se guarda en una variable llamada
    all_lines. Se cierra el archivo 4_dna_Sequences.txt contenido en la variable file y se abre el que será el nuevo
    archivo que contendrá las secuencias en formato fasta (en este caso se llama dna_sequences.fasta). Se modifican las
    secuencias que se tenían de forma que todas estén en mayúsculas, sin guiones y que el nombre de la secuencia y las
    bases estén en variables distintas (esto se hace con ayuda de un for). Dentro del loop se arma el formato fasta
    dentro del archivo que creamos (añadiendo el signo "> ", el nombre de la secuencia, un salto de línea y la
    secuencia correspondiente). Al final, se cierra el archivo de texto con las secuencias con un formato de tipo fasta.

GITHUB LINK
    Liga de GitHub donde se encuentra el programa:
    https://github.com/Danigore25/python_class/blob/master/src/Creacion_archivo_fasta.py

'''


# 1. Se abre el archivo 4_dna_sequences.txt que se encuentra en la carpeta docs de python_class (con el directorio
# "../docs/4_dna_sequence.txt").
file = open("data/4_dna_sequences.txt")

# 2. Se leen las líneas contenidas en el archivo, y se guardan en la variable all_lines.
all_lines = file.readlines()

# 3. Se cierra el archivo 4_dna_sequences.txt que se había guardado en la variable file.
file.close()

# 4. Se abre un archivo nuevo (en este caso se llamará dna_sequences.fasta).
new_file = open("dna_sequences.fasta", "w")

# 5. Se realiza un for que irá recorriendo las líneas contenidas en el archivo anterior.
for line in all_lines:
    line = line.replace("-", "")    # Esta línea reemplaza los guiones de una de las secuencias por nada.
    line = line.replace('"', '')     # Esta línea reemplaza las comillas por nada.
    sequences = line.split(" = ")    # Esta línea divide la cadena de cada secuencia en dos partes gracias al split.
    name = sequences[0]    # Esta línea guarda la cadena de cada secuencia que contiene el nombre de la misma.
    # Hay que recalcar que sequences tiene dos elementos: en 0 se tiene el nombre de la secuencia, y en 1 las bases.
    nucleotides = str(sequences[1]).upper()    # Esta línea guarda la cadena de la secuencia que contiene los
    # nucleótidos. Asimismo, se convierte la secuencia de nucleótidos a mayúsculas y se guarda.
    new_file.write("> " + name + "\n" + nucleotides)    # Aquí se guardan las secuencias modificadas en el archivo
    # fasta que acabamos de crear (guardado en la variable new_file).

# 6. Se cierra el archivo nuevo (en este caso, se encuentra escrito en new_file).
new_file.close()
