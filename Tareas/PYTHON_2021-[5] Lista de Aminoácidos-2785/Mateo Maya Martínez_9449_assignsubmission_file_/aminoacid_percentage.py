'''
NAME
       [aminoacid_percentage].py

VERSION
        [1.0]

AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>

DESCRIPTION
        [Este programa recibe como input un una secuencia protéica y una lista de aminoácidos y calcula el porcentaje de
        de los aminoácidos de la lista que están presentes en la secuencia]
CATEGORY
       [Protein sequence.]

USAGE
       [De uso bioinformático. Corre en python.
        La secuencia protéica debe ser introducida sin comillas
        Los aminoácidos deben ser introducidos separándolos por espacios.]

OPTIONS
       [Este programa no tiene opciones.]

EXAMPLES
       [Input: MSRSLLLRFLLFLLLLPPLP
               M L])
        Output: El porcentaje es: 55.0 %]

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/aminoacid_percentage.py]

'''

# Esta función procesará la lista, la secuencia y hara el cálculo del porcentaje de los aminoácidos
def get_aa_percentage (protein, aa_list = ['A','I','L','M','F','W','Y','V']):
    protein = protein.upper()
    longitud = len(protein)
    suma_porcentajes = 0
    for aa in aa_list:
        aa = aa.upper()
        ocurrencias = protein.count(str(aa))
        porcentaje = ocurrencias/longitud * 100
        suma_porcentajes += porcentaje
    return suma_porcentajes

#Pedir al usuario la secuencia protéica.
print ("Introduzca la secuencia protéica: ")
protein_input= input().strip()

#Pedir al usuario la lista de aminoácidos
print ("Introduzca la lista de aminoácidos (solo escriba el single letter code separados por espacios): ")
aa_input = input().split()

#Si la secuencia de aminoácidos no es especificada, se usará el default como argumento.
if len(aa_input) == 0:
    print (get_aa_percentage(protein_input))

#Si sí es especificada, usará la lista ingresada por el usuario como argumento.
else :
    print("El porcentaje es: ", ( get_aa_percentage(protein_input, aa_input)),"%")

#Algunas pruebas que tiene que pasar la función.
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65



