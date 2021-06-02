"""

NAME
        transcript_finder.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

DESCRIPTION
        Prints the positions of the triplets that encode the first start codon and the first stop codon of a
        DNA sequence, and prints the transcript sequence between those codons.

CATEGORY
        DNA transcription
        RNA

USAGE
        python transcript_finder.py

ARGUMENTS


EXAMPLES
        Example 1: Write the sequence 'TATTACTCCATACCTACCATTAAAAA' as input when the message
        "Escribe tu secuencia de DNA: " has been printed on the screen

        Usage: $ python transcript_finder.py

        Output:
        Escribe tu secuencia de DNA: TATTACTCCATACCTACCATTAAAAA
        El primer codon de inicio TAC empieza en la posicion 3 y el primer codon de paro ATT termina en la posicion 20
        La secuencia del transcrito (RNA) desde el codon de inicio hasta el codon de paro es:  AUGAGGUAUGGAUGGUAA

"""

# Solicitar secuencia
dna_seq = input("Escribe tu secuencia de DNA: ")

# Realizar la busqueda del codon de inicio y los codones de paro
start_post = 0
stop_post = 0
stop_name = ''
start_post = dna_seq.find("TAC", start_post)

# No buscar codones de paro si no hay un codon de inicio
if start_post != -1:
    stop_1 = dna_seq.find("ATT", start_post)
    stop_2 = dna_seq.find("ATC", start_post)
    stop_3 = dna_seq.find("ACT", start_post + 2)

    # Si no hay codones de paro la posicion del codon de paro sera igual -1
    if stop_1 == stop_2 and stop_2 == stop_3:
        stop_post = -1
    # Ordenar los codones de paro ascendentemente
    else:
        stop_codons = [stop_1, stop_2, stop_3]
        not_order = 1
        index = 0
        temp_val = 0

        # Ordenar los codones mientras no esten ordenados
        while not_order:
            not_order = 0
            index = 0

            # Ordenar codones
            while index < 2:
                if stop_codons[index] > stop_codons[index + 1]:
                    temp_val = stop_codons[index]
                    stop_codons[index] = stop_codons[index + 1]
                    stop_codons[index+1] = temp_val
                    not_order = 1
                index += 1

        # Buscar cual es el primer codon de paro
        index = 0
        while index < 3:
            # Asignar a stop_post el valor del primer codon de paro y a stop_name el triplete correspondiente
            if stop_codons[index] != -1:
                stop_post = stop_codons[index]
                index = 3
                if stop_post == stop_1:
                    stop_name = 'ATT'
                elif stop_post == stop_2:
                    stop_name = 'ATC'
                else:
                    stop_name = 'ACT'
            index += 1

# Imprimir el resultado obtenido
if start_post == -1:
    print("No se encontro un codon de inicio")
elif stop_post == -1:
    print("No se encontro un codon de paro despues del codon de inicio")
else:
    # Obtener la secuencia de RNA
    rna_seq = dna_seq[start_post:stop_post + 3]
    rna_seq = rna_seq.replace('A', 'U')
    rna_seq = rna_seq.replace('T', 'A')
    rna_seq = rna_seq.replace('G', 'X')
    rna_seq = rna_seq.replace('C', 'G')
    rna_seq = rna_seq.replace('X', 'C')

    # Imprimir el inicio y fin del transcrito, y la secuencia del transcrito
    print("El primer codon de inicio TAC empieza en la posicion", start_post,
          "y el primer codon de paro", stop_name, "termina en la posicion", stop_post + 2)
    print("La secuencia del transcrito (RNA) desde el codon de inicio hasta el codon de paro es:", rna_seq)
