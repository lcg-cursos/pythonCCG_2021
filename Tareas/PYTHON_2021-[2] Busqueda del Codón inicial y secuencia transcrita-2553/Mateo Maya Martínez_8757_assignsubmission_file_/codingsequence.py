'''
NOMBRE
       codingsequence.py
VERSION
        [1.0]
AUTOR
        Mateo Maya Martínez <matteo.mayam@icloud.com>
DESCRIPCIÓN
        [Este programa encuentra el fragmento codificante de una secuencia dada. Toma TAC como el codón de inicio y TAA como el codón de paro]
CATEGORÍA
       [Genomic sequence.]
USO

OPCIONES
'''

dna = 'AAGGTACGTCGCGCGTTATTAGCCTAAT'
start = dna.find("TAC")
end = dna.find("TAA")

print ("El codón de inicio empieza en la posición", start+1) #Es la variable start +1 porque el usuario no cuenta desde 0.
print ("El codón de paro empieza en la posición", end+1)#Es la variable end +1 porque el usuario no cuenta desde 0.
print ("La secuencia codificante es", dna[start:end + 3])