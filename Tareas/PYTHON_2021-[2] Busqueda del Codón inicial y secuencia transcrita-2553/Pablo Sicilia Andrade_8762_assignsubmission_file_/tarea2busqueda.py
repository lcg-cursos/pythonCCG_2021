"""
NAME
  tarea2busqueda.py

VERSION
  [1.0]

AUTHOR
  Pablo Sicilia Andrade  <psicilia@lcg.unam.mx>
  [Other authors]: [Modifications]


DESCRIPTION
  buscar trasncritos en una secuencia de DNA

CATEGORY
  sequence analysis

USAGE
  python tarea2busqueda.py

ARGUMENTS

INPUT

OUTPUT


EXAMPLES
  Example 1: la secuencia en dna AAGGATGTCGCGCGTTATTAGCCTAA, y el transcrito resultante AUGUCGCGCGUUAUUAGCCUAA

"""

dna = 'AAGGATGTAATCGCGCGTTATTAGCCTAA'
met_ini = 'AUG'
fin_seq = 'UAA'
rna = dna.replace('T','U')
inicio = rna.find(met_ini)
fin = rna.find(fin_seq)
print('la secuencia de RNA es: ', rna)
print('AUG se encuentra en la posicion: ',inicio)
print('TAA se encuentra en la posicion: ',fin)
print('El transcrito es: ',rna[inicio:fin+3])

