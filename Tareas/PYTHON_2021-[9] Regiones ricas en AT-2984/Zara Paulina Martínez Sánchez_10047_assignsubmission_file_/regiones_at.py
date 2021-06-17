"""
## NAME

        regiones_at.py

## VERSION

        [1.0]

## AUTHOR

        Zara Paulina Martinez Sanchez < zaram042001 @ gmail.com >

## DATE

        [08/06/2021]

## DESCRIPTION

        Programa que analiza una secuencia de DNA para buscar regiones ricas en AT
        las cuales contengan 5 o mas As y/o Ts. En caso de contener en la secuencia
        caracteres diferentes a ATGC se le notifica al usuario

## CATEGORY

        Sequence analysis


## USAGE

        regiones_at.py no requiere argumentos

## FUNCTIONS

        def analizar_sec(seq):
            no_bases = re.findall(r"[^ATGC]", seq)
            region_at = re.findall(r"[AT]{5,}", seq)
            try:
                if no_bases:
                    raise ValueError
            except ValueError:
                print(f'La secuencia que ingresó cuenta con caracteres no validos: {no_bases}')
            else:
                if region_at:
                    print(f'Las regiones ricas en AT son: {region_at}')
                else:
                    print("No existen regiones ricas en AT en su secuencia")

## EXAMPLES

        Input:
        CTGCATTATATCGTACGAAATTATACGCGCG

        Output:
        Las regiones ricas en AT son: ['ATTATAT', 'AAATTATA']

## GITHUB LINK

        https://github.com/zara-ms/python_class/tree/master/src

"""

# Libreria a usar
import re


def analizar_sec(seq):
    no_bases = re.findall(r"[^ATGC]", seq)
    region_at = re.findall(r"[AT]{5,}", seq)

#   Reconocer caracteres invalidos y marcar error
    try:
        if no_bases:
            raise ValueError

    except ValueError:
        print(f'La secuencia que ingresó cuenta con caracteres no validos: {no_bases}')

#   Buscar secuencias ricas en AT si la secuencia es correcta
    else:
        if region_at:
            print(f'Las regiones ricas en AT son: {region_at}')
        else:
            print("No existen regiones ricas en AT en su secuencia")


print("Ingrese la secuencia a analizar")
secuencia = input()
secuencia = secuencia.upper()

# Llamar a la funcion
analizar_sec(secuencia)
