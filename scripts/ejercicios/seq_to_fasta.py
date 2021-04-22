# Abir archivo
file = open("data/4_dna_sequences.txt")

# Leer todas las lineas y guardarlas en una lista
all_lines = file.readlines()

# Cerrar archivo
file.close()

# Abrir archivo para escribir
my_file = open("output/dna.fasta", "w")

# Usar esas lineas en un loop
for line in all_lines:
    line = line.replace("-","") # quita diagonales
    line = line.replace('"',"") # quita comillas
    seq = line.split(" = ") # separa el header de la secuencia
    # imprime en formato fasta con secuencias en mayusculas
    my_file.write("> " + seq[0] + "\n" + seq[1].upper())

my_file.close()

