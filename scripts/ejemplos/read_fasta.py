my_file = open("data/4_dna_sequences.txt", "r")
my_file_contents = my_file.read()
print(my_file_contents)
print(len(my_file_contents))

# Abir archivo
file = open("data/4_dna_sequences.txt", "r")

# Leer las lineas
for line in file:
  print("Length: " + str(len(line)) + " " + line)

# Cerrar archivo
file.close()
