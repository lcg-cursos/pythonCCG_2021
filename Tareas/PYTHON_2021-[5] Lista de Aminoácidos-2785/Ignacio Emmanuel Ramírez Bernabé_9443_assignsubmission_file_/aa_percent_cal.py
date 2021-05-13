"""

NAME
        aa_percent_cal.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/aa_percent_cal.py

DESCRIPTION
        This program calculates the percentage of a list of amino acids in a protein sequence

CATEGORY
        Amino acids
        Protein sequence
        Percentage

USAGE
        python aa_percent_cal.py

ARGUMENTS
        No command line arguments

EXAMPLES
        Example: Run the program and give the protein sequence and the list of amino acids as input

        Usage: $ python aa_percent_cal.py

        Input:
        Escribe tu secuencia proteica:
        MARAMAALM
        Escribe tu lista de aminoacidos separados por comas para el calculo de su porcentaje:
        A,F

        Output:
        El porcentaje de aminoacidos de la lista ['A', 'F'] en la secuencia MARAMAALM es: 44.44


"""
# Obtener el porcentaje de aminoacidos


def get_aa_percentage(seq, aa_to_find=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    aa_sum = 0

    # Usar la lista de aa default si no se tienen aa en la lista original
    if aa_to_find[0] == '':
        aa_to_find[0] = 'A'
        for amac in ['I', 'L', 'M', 'F', 'W', 'Y', 'V']:
            aa_to_find.append(amac)

    # Obtener la cantidad de aminoacidos encontrados en la secuencia
    for amino in aa_to_find:
        aa_sum += seq.count(amino)

    # Obtener tamano de la secuencia y calcular el porcentaje
    length = len(seq)
    percent = round((aa_sum/length)*100, 2)

    return percent


# Lista de 20 aminoacidos
all_aa = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']

# Obtener secuencia proteica
aa_seq = input("Escribe tu secuencia proteica: \n")

# Verificar si la secuencia esta vacia
if aa_seq == '':
    print("No se escribio ninguna secuencia")
    exit(1)

# Revisar si la secuencia esta mal
for char in aa_seq:
    is_valid = 0
    i = 0

    # Buscar si alguno de los 20 aa coincide con cada aa de la secuencia
    while is_valid == 0:
        while i < 20:
            if char == all_aa[i]:
                is_valid = 1
                i = 20
            i += 1
        # Terminar el proceso si la secuencia no es valida
        if is_valid == 0:
            print("La secuencia no es valida")
            exit(1)


# Obtener string de la lista de aminoacidos
aa_raw_list = input("Escribe tu lista de aminoacidos separados por comas para el calculo de su porcentaje: \n")

# Convertir el string en lista si es de un solo elemento
if len(aa_raw_list) == 1:
    aa_raw_list = [aa_raw_list]
# Obtener elementos de la lista separados por ','
else:
    aa_raw_list = aa_raw_list.split(',')
    if len(aa_raw_list[0]) > 1:
        print("La lista no es valida")
        exit(1)

# Crear lista de aminoacidos vacia
aa_list = []

# Obtener los aminoacidos de la lista
if aa_raw_list[0] == '':
    aa_list = aa_raw_list
else:
    for element in aa_raw_list:
        is_valid = 0
        for aa in all_aa:
            if element == aa:
                aa_list.append(aa)
                is_valid = 1
        if is_valid == 0:
            print("La lista no es valida")
            exit(1)

# Revisar si los aminoacidos de la lista no se repiten
for aa in aa_list:
    num_aa = aa_list.count(aa)
    if num_aa > 1:
        print("La lista no es valida")
        exit(1)

# Obtener porcentaje
percentage = get_aa_percentage(aa_seq, aa_list)

# Imprimir resultado
print(f'El porcentaje de aminoacidos de la lista {aa_list} en la secuencia {aa_seq} es: {percentage}\n')
