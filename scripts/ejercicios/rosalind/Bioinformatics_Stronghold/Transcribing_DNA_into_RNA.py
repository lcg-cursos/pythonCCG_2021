# Dna seq
#dna = 'AATGGTTTAACACGTAAACGGTCGG'
dna = input('Secuencia de DNA: ')
# Replacing T for U
dna = dna.replace('T', 'U')

# Checar que los resultados sean iguales
# dna == 'GAUGGAACUUGACUACGUAAAUU'
print(dna)
