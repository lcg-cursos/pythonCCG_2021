"""
NAME 
    tarea_9_regiones_AT.py

VERSION
    1.0

AUTHOR
    Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
    imprimir las regiones ricas en AT si solo hay ATCG 
    en caso contrario imprime los caracteres incorrectos 


CATEGORY
    secuence analysis

USAGE
    python tarea_9_regiones_AT.py
  
ARGUMENTS
    none

    
INPUT
    CTGCATTATATCGTACGAAATTATACGCGCG

OUTPUT
    ['ATTATAT', 'TA', 'AAATTATA']

GITHUB
    https://github.com/psicilia/python_Class/blob/d739f3c133d25d8b7e53b24d5b465c88d0df3404/src/tareas/tarea_9_regiones_AT.py

"""
import re 

dna = "CTGCATTATATCGTACGAAATTATACGCGCG"
#dna = input('ingrese la cadena a analizar')
dna = dna.upper().replace(" ", "")
#leemos la cadena de dna, eliminamos espacios y convertimos en mayusculas 

class NotATCG(Exception):
    pass
#definimos nuestro error 

try:

    if (re.search(r"[^ATCG]", dna)):
        raise NotATCG('sequence contains invalid elements')
    #verificamos si solo contiene ATCG
except NotATCG:
    errors =  re.findall(r"[^ATCG]", dna)
    print(errors)
    #En caso de encontrar caracteres diferentes imprimimos la lista de caracteres que no coinsiden
else:
    matches = re.findall(r"[AT][AT]+", dna)
    print(matches)
    #si la secuencia solo contiene ATCG imprimimos los segemntos que conteinen AT de 2 o mas
