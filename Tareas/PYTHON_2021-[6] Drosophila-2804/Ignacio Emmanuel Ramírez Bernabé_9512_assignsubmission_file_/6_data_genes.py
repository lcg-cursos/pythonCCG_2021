"""

NAME
        6_data_genes.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/6_data_genes.py

DESCRIPTION
        This program get information about the genes in the 6-data.csv file and print those that fulfill certain cases

CATEGORY
        Drosophila
        Genes
        DNA

USAGE
        python 6_data_genes.py

ARGUMENTS
        No command line arguments

EXAMPLES
        Example 1:  Run the program in the same directory as the 6-data.csv file

        Usage: $ python 6_data_genes.py

        Input:
        6-data.csv

        Output:
        Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:
        kdy647
        jdg766
        kdy533

        Genes de entre 90 y 110 bases de longitud:
        kdy647
        teg436

        Genes cuyo contenido de AT es inferior a 0,5 y cuyo nivel de expresión es superior a 200:
        teg436

        Genes cuyo nombre comienza con 'k' o 'h', y que no pertenecen a Drosophila melanogaster:
        kdy533
        hdt739
        hdu045

        Nivel del contenido de AT de los genes:
        El gen kdy647 tiene un contenido de AT alto
        El gen jdg766 tiene un contenido de AT medio
        El gen kdy533 tiene un contenido de AT medio
        El gen hdt739 tiene un contenido de AT bajo
        El gen hdu045 tiene un contenido de AT medio
        El gen teg436 tiene un contenido de AT medio


"""

# Abrir archivo y leer lineas
file = open("6-data.csv")
lines = file.readlines()
file.close()

# Crear lista de cada gene con su informacion
genes = []
for line in lines:
    line = line.replace('\n', '')
    line = line.split(',')
    genes.append(line)

# Crear lista donde se guardaran los resultados
results = [[], [], [], [], []]

# Obtener los resultados
for gen in genes:
    # Calcular la longitud de la secuencia
    length = len(gen[1])

    # Calcular contenido de AT
    at_content = (gen[1].count('a') + gen[1].count('t')) / length

    # Revisar si el gene pertenece a cierta especie y guardar el gene
    if gen[0] == "Drosophila melanogaster":
        results[0].append(gen[2])
    elif gen[0] == "Drosophila simulans":
        results[0].append(gen[2])

    # Guardar el gene si cumple con un rango de tamano
    if 90 < length < 110:
        results[1].append(gen[2])

    # Guardar el gene si su contenido de AT es menor a 0.5 y su nivel de expresion mayor a 200
    if at_content < 0.5 and int(gen[3]) > 200:
        results[2].append(gen[2])

    # Guardar el gene si comienza con k o h, y si es de la especie Drosophila melanogaster
    if gen[2][0] == 'k' or gen[2][0] == 'h':
        if gen[0] != "Drosophila melanogaster":
            results[3].append(gen[2])

    # Obtener el nivel del contenido de AT, y guardar el resultado
    if at_content > 0.65:
        at_level = "alto"
    elif at_content < 0.45:
        at_level = "bajo"
    else:
        at_level = "medio"

    results[4].append(f'El gen {gen[2]} tiene un contenido de AT {at_level}')

# Imprimir los genes que pertenecen a Drosophila melanogaster o Drosophila simulans
print("Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:")
for result in results[0]:
    print(result)

# Imprimir los genes de entre 90 y 110 bases de longitud
print("\nGenes de entre 90 y 110 bases de longitud:")
for result in results[1]:
    print(result)

# Imprimir los genes cuyo contenido de AT sea menor a 0.5 y cuyo nivel de expresión sea superior a 200
print("\nGenes cuyo contenido de AT es inferior a 0,5 y cuyo nivel de expresión es superior a 200:")
for result in results[2]:
    print(result)

# Imprimir los genes cuyo nombre comience con "k" o "h", excepto los que pertenecen a Drosophila melanogaster
print("\nGenes cuyo nombre comienza con 'k' o 'h', y que no pertenecen a Drosophila melanogaster:")
for result in results[3]:
    print(result)

# Imprimir el gen y si su contenido de AT es alto (mayor que 0.65), bajo (menor que 0.45) o medio (entre 0.45 y 0.65)
print("\nNivel del contenido de AT de los genes:")
for result in results[4]:
    print(result)
