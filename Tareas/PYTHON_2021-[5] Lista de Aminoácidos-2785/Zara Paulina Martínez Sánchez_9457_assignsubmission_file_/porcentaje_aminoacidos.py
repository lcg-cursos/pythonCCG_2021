"""
## NAME
        porcentaje_aminoacidos.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

        12/05/2021

## DESCRIPTION

        Este programa utiliza una función para calcula el porcentaje de aminoácidos hidrofílicos
       en una proteina dada por el usuario.

## CATEGORY

        Protein sequence

## USAGE

        porcentaje_aminoacidos.py es de uso bioinformático

## ARGUMENTS

        No hay argumentos

## EXAMPLES
        Input:
            "MSRSLLLRFLLFLLLLPPLP"
        Output:
            "El porcentaje de aminoacidos hidrofílicos en la proteina es: 65"

## GITHUB LINK
        https://github.com/zara-ms/python_class/tree/master/src

"""

# Obtener el porcentaje de aminoacidos de una lista dada en una proteina especifica
def get_aa_content(proteina, lista_aa):
    total = len(proteina)
    porcentaje = 0
    for aa in lista_aa:
        aa_count = proteina.upper().count(aa)
        porcentaje += aa_count * 100 / total
    return porcentaje

# Definir la lista de aminoacidos hidrofilicos
aa_hidrofilicos = ['A','I','L','M','F','W','Y','V']

# Probar que el codigo funcione de manera adecuada al obtener los resultados esperados
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_content("MSRSLLLRFLLFLLLLPPLP", aa_hidrofilicos) == 65

# Ingresar la proteina a analizar y guardarla en una nueva variable
print("Introduzca la proteina que desea analizar")
proteina_nueva = input()
print("El porcentaje de aminoacidos hidrofílicos en la proteina es: "
      + str(get_aa_content(proteina_nueva, aa_hidrofilicos)))
