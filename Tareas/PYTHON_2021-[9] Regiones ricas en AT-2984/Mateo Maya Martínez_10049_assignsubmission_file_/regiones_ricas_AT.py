'''
NAME
       [regiones_ricas_AT].py
VERSION
        [1.0]
AUTHOR
        Mateo Maya Martínez <[matteo.mayam@outlook.com>
DESCRIPTION
        [Este programa busca regiones ricas en AT en una secuencia de DNA y ocupa manejo de errores si se encuentran letras distintas a ATCG.]
CATEGORY
       [Sequence.]
USAGE
       [De uso bioinformático. Corre en python.]
OPTIONS
       [Este programa no tiene opciones.]
EXAMPLES
       [Input: CTGhCATTATATCGTACnGAAATTATACGCGCG
        Output: Su secuencia tiene la(s) siguiente(s) base(s) rara(s): ['h', 'n']
                Las regiones ricas en AT son: ['ATTATAT', 'AAATTATA'] ]
LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/regiones_ricas_AT.py]
'''

#Importación de librerías.
import re

#Función que verifica que no haya letras diferentes de ATCG en la secuencia, si las hay, imprime un mensaje, pero el código continúa.
def verify (dna):
    error = re.findall(r"[^ATGC]", dna)
    try:
        if  re.search(r"[^ATGC]", dna):
            raise ValueError

    except ValueError as ex:
        print (f"Su secuencia tiene la(s) siguiente(s) base(s) rara(s): {error}")


#Función que identifica regiones ricas e AT
def AT_regions (dna):

    region_AT = re.findall("[AT]{5,}", dna)
    if region_AT:
        print(f"Las regiones ricas en AT son: {region_AT}")

    else:
        print ("Su secuencia no tiene regiones ricas en AT")

#Pedir al usuario que ingrese su secuencia.
dna = input("Introduce tu secuencia:\n")

#Llamada de las funciones.
verify(dna)
AT_regions(dna)