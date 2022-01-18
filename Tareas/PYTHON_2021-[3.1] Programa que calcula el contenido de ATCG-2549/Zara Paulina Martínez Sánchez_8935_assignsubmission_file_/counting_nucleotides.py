"""
## NAME
    counting_nucleotides.py

## VERSION

    [0.0]

## AUTHOR

    Zara Paulina Martinez Sanchez <zaram042001@gmail.com>

## DATE

    21/04/2021

## DESCRIPTION

    Este programa cuenta el numero de A, T, C y G dentro de una secuencia de DNA

## CATEGORY

    Sequence analysis

## USAGE

    counting_nucleotides.py no cuenta con mas opciones

## ARGUMENTS
    No hay argumentos

## EXAMPLES
    Input:
        ATCGAATCCCTAGGACCTTAAGAGACTA
    Output:
        El número de nucleótidos es de
        As: 10
        Cs: 7
        Gs: 5
        Ts: 6

## GITHUB LINK

    https://github.com/zara-ms/python_class/tree/master/src

"""
# Pedir la secuencia y contar el contenido de cada nucleotido
print("Inserte una secuencia de DNA\n")
sec = input()
sec = sec.upper()  # Asegurar que el input se encuentre en mayusculas
num_a = sec.count("A")
num_t = sec.count("T")
num_g = sec.count("G")
num_c = sec.count("C")
print(f'El número de nucleótidos es de\nAs: {num_a}\nCs: {num_c}\nGs: {num_g}\nTs: {num_t}')
