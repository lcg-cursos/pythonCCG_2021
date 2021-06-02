'''
NAME
    Drosophila.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa toma un archivo ya existente con genes de varias especies de Drosophila y muestra outputs
    dependiendo de ciertas condiciones dadas, en este caso imprime los nombres de los genes pertenecientes a Drosophila
    melanogaster o simulans, los genes que tienen una secuencia de entre 90 y 110 bases de longitud, los genes con un
    contenido de AT inferior a 0.5 y nivel de expresión superior a 200, los genes cuyo nombre empiece con k o h pero no
    pertenezcan a Drosophila melanogaster, y por último menciona para cada gen si su contenido de AT es alto, medio o
    bajo.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Drosophila.py [sin opciones]

ARGUMENTS
    [sin argumentos]

INPUT
    6-data.csv (archivo que contiene las secuencias de DNA)

OUTPUT
    Gen perteneciente a Drosophila melanogaster: kdy647
    El gen kdy647 tiene 109 bases de longitud
    El gen kdy647 tiene un contenido de AT alto
    Gen perteneciente a Drosophila melanogaster: jdg766
    El gen jdg766 tiene un contenido de AT medio
    Gen perteneciente a Drosophila simulans: kdy533
    El gen kdy533 comienza con k o con h y no pertenece a Drosophila melanogaster
    El gen kdy533 tiene un contenido de AT medio
    El gen hdt739 comienza con k o con h y no pertenece a Drosophila melanogaster
    El gen hdt739 tiene un contenido de AT bajo
    El gen hdu045 comienza con k o con h y no pertenece a Drosophila melanogaster
    El gen hdu045 tiene un contenido de AT medio
    El gen teg436 tiene 98 bases de longitud
    El gen teg436 tiene un contenido de AT menor que 0.5 y un nivel de expresión mayor que 200
    El gen teg436 tiene un contenido de AT medio


EXAMPLES
    Example 1: Se tiene el archivo 6-data.csv, el cual contiene datos acerca de genes encontrados en distintas especies
    de Drosophila. Primero se abrirá y leerá el archivo, guardando la información en el programa. Antes de analizar los
    datos, primero se va a definir una función que va a ayudar a calcular el contenido de AT de cada gen. Después se va
    a realizar un loop que dividirá las líneas en el archivo (con los campos de cada gen separados por comas), de forma
    que se creará una lista por cada uno de los genes. Se va a evaluar cada uno de esos genes dependiendo de sus datos
    a partir de distintas condiciones (leer descripción), si se cumple la condición se mencionarán hechos sobre el gen.

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/Drosophila.py

'''

# 1. Abrir archivo 6-data.csv que se encuentra en el directorio "../docs/6-data.csv", guardar la información.
file = open("../docs/6-data.csv")
lines = file.readlines()
file.close()


# 2. Definir función que calcule el contenido de AT.
def get_at_content(dna):
    length = len(dna)
    a_count = dna.count('a')
    t_count = dna.count('t')
    at_content = (a_count + t_count)/length
    return at_content


# 3. Hacer un loop que separe la información de acuerdo a la delimitación de sus campos por comas.
for line in lines:
    sequences = line.split(",")

# 4. Imprimir los nombres de los genes pertenecientes a Drosophila melanogaster o simulans.
    if sequences[0] == 'Drosophila melanogaster' or sequences[0] == 'Drosophila simulans':
        print("Gen perteneciente a " + str(sequences[0]) + ": " + str(sequences[2]))

# 5. Imprimir los nombres de los genes de entre 90 y 110 bases de longitud.
    if (len(sequences[1]) > 90) and (len(sequences[1]) < 110):
        print("El gen " + str(sequences[2]) + " tiene " + str(len(sequences[1])) + " bases de longitud")

# 6. Imprimir los nombres de los genes cuyo contenido de AT sea inferior a 0.5 y cuyo nivel de expresión sea superior a
# 200.
    if (get_at_content(sequences[1]) < 0.5) and (int(sequences[3]) > 200):
        print("El gen " + str(sequences[2]) + " tiene un contenido de AT menor que 0.5 y un nivel de expresión mayor "
                                              "que 200")

# 7. Imprimir los nombres de los genes cuyo nombre comience con "k" o "h", excepto los que pertenecen a Drosophila
# melanogaster.
    if (sequences[2].startswith('k') or sequences[2].startswith('h')) and not sequences[0] == 'Drosophila melanogaster':
        print("El gen " + str(sequences[2]) + " comienza con k o con h y no pertenece a Drosophila melanogaster")

# 8. Imprimir para cada gen un mensaje dando el nombre del gen y diciendo si su contenido de AT es alto (mayor que
# 0.65), bajo (menos de 0.45) o medio (entre 0.45 y 0.65).
    if get_at_content(sequences[1]) > 0.65:
        print("El gen " + str(sequences[2]) + " tiene un contenido de AT alto")
    elif get_at_content(sequences[1]) < 0.45:
        print("El gen " + str(sequences[2]) + " tiene un contenido de AT bajo")
    else:
        print("El gen " + str(sequences[2]) + " tiene un contenido de AT medio")
