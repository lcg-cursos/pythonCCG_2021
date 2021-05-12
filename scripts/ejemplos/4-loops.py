# 1. Abrir nuestro archivo 4_dna_sequences.txt

# 2. Leer todas las lineas y las guardamos en una variable (lista)

# 3. Cerrar el archivo 4_dna_sequences.txt

# 4. Abrir el archivo file.fasta para escribir el resultado usando open("file.fasta", "w")

# 5. FOR para todas las lineas:
#       Quitar lineas "-" con replace("-","")
#       Quitar las '"' con replace('"', "")
#       Cambiar las secuencias a mayusculas con upper()
#       Dividir el nombre y la secuencia con slipt(" = ")
#       Escribir en formato fasta file.write("> " + nombre + "\n" + secuencia)

# 6. Cerrar el archivo file.fasta