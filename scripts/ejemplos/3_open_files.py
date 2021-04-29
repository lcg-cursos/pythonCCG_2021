# Nombre del archivo
my_file_name = "data/dna.txt"

# Abrir
my_file = open(my_file_name)

# Leer
my_file_content = my_file.read()

# Quitar el salto de linea
my_dna = my_file_content.rstrip("\n")

# Imprimir mensaje
print("Longitud de DNA: " + str(len(my_dna)))