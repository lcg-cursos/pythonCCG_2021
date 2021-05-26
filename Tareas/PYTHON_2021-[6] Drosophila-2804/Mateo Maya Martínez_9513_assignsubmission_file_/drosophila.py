'''
NAME
       [drosophila].py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>

DESCRIPTION
        [Este programa recibe como input un archivo .csv y a partir de él responde ciertas preguntas.]

CATEGORY
       [Organism.]

USAGE
       [De uso bioinformático. Corre en python.
       El programa lee el archivo 6-data.csv.
       El archivo está ubicado en siguiente ruta relativa: ../docs/6-data.csv]

OPTIONS
       [Este programa no tiene opciones.]

EXAMPLES
       [Input file: 6-data.csv
        Output: Los genes que pertenecen a D. melanogaster o D. simulans son:
                ...
                Los genes con una longitud de entre 90 y 110 nucleótidos son:
                ...
                Los genes con un contenido de AT inferior a 0.5 y un nivel de expresión mayor a 200 son:
                ...
                Los genes cuyo nombre empieza con 'k' o 'h' exceptuando los que pertenecen a D. melanogaster son:
                ...
                La respuesta a la pregunta 5 es:
                ...]

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/drosophila.py]
'''

#Abrir y leer el archivo con el cual trabajaremos.
input_file = open("../docs/6-data.csv")
input_file_lines = input_file.readlines()
input_file.close()

#Esta función procesa las líneas y si cumplen la condición imprime el nombre de los genes
def first_question(input_file_lines):
    for line in input_file_lines:
        line_list = line.split(",")
        name = line_list[2]
        if line.startswith("Drosophila melanogaster") or line.startswith("Drosophila simulans"):
            print(name)

#Esta función procesa las líneas y si cumplen la condición imprime el nombre de los genes
def second_question(input_file_lines):
    for line in input_file_lines:
        line = line.split((","))
        sequence = len(line[1])
        if sequence >= 90 and sequence <= 110:
            print(line[2])

#Esta función procesa las líneas, calcula el contenido de AT y si cumplen la condición imprime el nombre de los genes
def third_question(input_file_lines):
    for line in input_file_lines:
        line = line.split((","))
        expression = int(line[3])
        sequence = line[1]
        A_percentage = line[1].count("a")
        T_percentage = line[1].count("t")
        AT_percentage = round((A_percentage + T_percentage)/ len(sequence), 2)

        if AT_percentage <= 0.5 and int(expression) > 200:
            print(line[2])

#Esta función procesa las líneas y si cumplen la condición imprime el nombre de los genes
def fourth_question(input_file_lines):
    for line in input_file_lines:
        line = line.split((","))
        organism = line[0]
        name = line[2]
        if ((name.startswith("k") or name.startswith("h")) and organism != ("Drosophila melanogaster")):
            print(name)

'''Esta función procesa las líneas, calcula el contenido de AT y dependiendo de la condición que cumplan imprime un 
mensaje diferente.'''

def fifth_question(input_file_lines):
    for line in input_file_lines:
        line = line.split((","))
        sequence = line[1]
        name = line[2]
        A_percentage = sequence.count("a")
        T_percentage = sequence.count("t")
        AT_percentage = round((A_percentage + T_percentage) / len(sequence), 2)

        if AT_percentage > 0.65:
            print(f"El contenido de AT del gen {name} es alto")
        elif AT_percentage < 0.45:
            print(f"El contenido de AT del gen {name} es bajo")
        elif AT_percentage > 0.45 and AT_percentage < 0.65:
            print(f"El contenido de AT del gen {name} es medio")

#Imprimir un mensaje para saber a qué pregunta corresponde cada respuesta junto con lo que imprime cada función.
print("Los genes que pertenecen a D. melanogaster o D. simulans son:")
first_question(input_file_lines)

print ("\nLos genes con una longitud de entre 90 y 110 nucleótidos son:")
second_question(input_file_lines)

print ("\nLos genes con un contenido de AT inferior a 0.5 y un nivel de expresión mayor a 200 son:")
third_question(input_file_lines)

print ("\nLos genes cuyo nombre empieza con 'k' o 'h' exceptuando los que pertenecen a D. melanogaster son:")
fourth_question(input_file_lines)

print ("\nLa respuesta a la pregunta 5 es:")
fifth_question(input_file_lines)