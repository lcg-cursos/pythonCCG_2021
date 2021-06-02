'''
NAME
    Lista_aminoacidos.py

VERSION
    1.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa calcula el porcentaje de aminoácidos hidrofílicos (por default) en una secuencia proteica.

CATEGORY
    Análisis de secuencias proteicas

USAGE
    python Lista_aminoacidos.py

ARGUMENTS
    [sin argumentos]

INPUT
    Secuencia proteica, lista de aminoácidos

OUTPUT
    Porcentaje del aminoácido en la secuencia


EXAMPLES
    Example 1: Se tiene la secuencia proteica MSRSLLLRFLLFLLLLPPLP, y la lista de aminoácidos es ["M"]. El programa
    primero evalúa si la lista que le dimos es igual la lista default que se tiene de secuencias de aminoácidos. Si no
    es así, entonces se utilizan los valores de la lista dada por el usuario y así calcula el porcentaje de los
    aminoácidos de la lista. Si sí se cumple que los elementos de la lista son iguales a los elementos default, entonces
    se toma la secuencia default y así se calcula el porcentaje de los mismos con la secuencia dada por el usuario. En
    este caso, tendríamos que el porcentaje del aminoácido M dentro de la secuencia es igual a 5.

    Example 2: Tomando en cuenta la explicación anterior, tenemos que la secuencia de aminoácidos es
    MSRSLLLRFLLFLLLLPPLP, mientras que la lista de aminoácidos que se van a contar es ['F', 'S', 'L']. En este caso, el
    porcentaje de los aminoácidos en la lista dada por el usuario dentro de la secuencia proteica sería 70.

GITHUB LINK
    https://github.com/Danigore25/python_class/blob/master/src/Lista_aminoacidos.py

'''


# 1. Crear función que calcule el porcentaje de los aminoácidos dados en una secuencia proteica.
def get_aa_percentage(protein, aa_list):

    # Escribir los aminoácidos default (que serán aminoácidos hidrofílicos).
    aa_default = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
    length = len(protein)
    aa_total = 0
    # Preguntar si la lista de aminoácidos dada por el usuario es igual a la default.
    if aa_list != aa_default:
        for amino_acid in aa_list:
            aa_count = protein.count(amino_acid)
            aa_content = (aa_count/length)*100
            aa_total += aa_content
        return aa_total
    else:
        for amino_acid in aa_default:
            aa_count = protein.count(amino_acid)
            aa_content = (aa_count/length)*100
            aa_total += aa_content
        return aa_total


# 2. Hacer testings de la función.
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']) == 65

# 3. Pedir al usuario una secuencia proteica.
print("Write a protein sequence (format: in cappital letters): ")
protein_input = input()

# 4. Pedir al usuario una lista de aminoácidos.
print("Write an amino acid list (format = [A, B, C, ...]): ")
list_input = input()

# 5. Imprimir el porcentaje de aminoácidos de la lista dentro de la secuencia proteica.
print("The percentage of " + list_input + " in the sequence " + protein_input + " is: "
      + str(get_aa_percentage(protein_input, list_input)) + " %")
