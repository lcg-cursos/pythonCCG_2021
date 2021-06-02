"""
## NAME
        genes_drosophila.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

        18/05/2021

## DESCRIPTION

        Este programa utiliza el archivo 6-data.csv ubicado en /python_class/data y proporciona
        información sobre los genes existentes

## CATEGORY

        Sequence analysis

## USAGE

        genes_drosophila.py es de uso bioinformático

## ARGUMENTS
        No hay argumentos

## EXAMPLES
        Input:
            archivo: 6-data.csv

        Output:
        "El gen kdy647 :
        Pertenece a Drosophila melanogaster
        Tiene entre 90 y 110 bases de longitud
        Tiene un contenido de AT alto

        El gen jdg766 :
        Pertenece a Drosophila melanogaster
        Tiene un contenido de AT medio

        El gen kdy533 :
        Pertenece a Drosophila simulans
        Tiene entre 90 y 110 bases de longitud
        Comienza con h o k y no pertenece a Drosophila melanogaster
        Tiene un contenido de AT medio

        El gen hdt739 :
        Comienza con h o k y no pertenece a Drosophila melanogaster
        Tiene un contenido de AT bajo

        El gen hdu045 :
        Comienza con h o k y no pertenece a Drosophila melanogaster
        Tiene un contenido de AT medio

        El gen teg436 :
        Tiene entre 90 y 110 bases de longitud
        Tiene un contenido de AT inferior a 0.5 y un nivel de expresión superior a 200
        Tiene un contenido de AT medio"

## GITHUB LINK
        https://github.com/zara-ms/python_class/tree/master/src

"""


# Determinar el contenido de AT
def at_content(secuencia):
    total = len(secuencia)
    t_num = (secuencia.lower()).count("t")
    a_num = (secuencia.lower()).count("a")
    content = (t_num + a_num) / total
    return content


# Guardar la informacion del archivo en una variable a usar
file = open("../data/6-data.csv", "r")
all_lines = file.readlines()
file.close()

for line in all_lines:
    line1 = line.split(",")
    print("El gen " + line1[2] + " :")
#   Obtener los genes del organismo que buscamos
    if line1[0] == "Drosophila melanogaster" or line1[0] == "Drosophila simulans":
        print("Pertenece a " + line1[0])

#   Obtener los genes de la longitud deseada
    if len(line1[1]) >= 90 and len(line1[1]) <= 110:
        print("Tiene entre 90 y 110 bases de longitud")

#   Obtener los genes con el contenido de AT deseado
    contenido = at_content(line1[1])
    expresion = int(line1[3])
    if contenido < 0.5 and expresion > 200:
        print("Tiene un contenido de AT inferior a 0.5 y un nivel de expresión superior a 200")

    if line1[0] != "Drosophila melanogaster" and (line1[2].startswith("k") or line1[2].startswith("h")):
        print("Comienza con h o k y no pertenece a Drosophila melanogaster")

# Determinar si el contenido de AT es alto, bajo o medio
    if contenido > 0.65:
        print("Tiene un contenido de AT alto")
    elif contenido < 0.45:
        print("Tiene un contenido de AT bajo")
    else:
        print("Tiene un contenido de AT medio")

    print("")
