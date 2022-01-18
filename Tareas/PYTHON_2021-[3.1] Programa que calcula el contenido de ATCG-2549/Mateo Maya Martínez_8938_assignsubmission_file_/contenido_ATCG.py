'''
NAME
       contenido_ATCG.py

VERSION
        [1.#]

AUTHOR
        Mateo Maya Martínez <matteo.mayam@outlook.com>

DESCRIPTION
        [Este programa calcula el contenido de cada uno de los nucleótidos (A, T, C y G) de una secuencia dada.]

CATEGORY
       [Genomic sequence.]


EXAMPLES
       [Ejemplo1. input: ATCG.
                  output: A: 1, T: 1, C: 1, G: 1]

LIGA DE GITHUB: [https://github.com/MateoMayaM/python_class/blob/master/src/contenido_ATCG.py]

'''

print ("Introduce una secuencia de DNA" + "\n")

dna = input()

A = dna.count("A")
C = dna.count("C")
G = dna.count("G")
T = dna.count("T")

conteo = "A:" + str(A) + ", " + "C:" + str(C) + ", " + "G:" + str(G) + ", " + "T:" + str(T)

print (conteo)
