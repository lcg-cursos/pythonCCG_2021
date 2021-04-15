# Agregar el nombre del archivo como variable
# Ruta: "../../data/dna.txt"
# Agregar el nombre del archivo como variable
my_file_name = "../../data/dna.txt"

# Leer el archivo
my_file = open(my_file_name)
my_file_contents = my_file.read()

# Quitar el caracter de nueva linea \n
my_dna = my_file_contents.rstrip("TC\n")

# Calular la longitud
dna_length = len(my_dna)

# Mostrar mensaje
print("The sequence is " + my_dna +  " and length is " + str(dna_length))