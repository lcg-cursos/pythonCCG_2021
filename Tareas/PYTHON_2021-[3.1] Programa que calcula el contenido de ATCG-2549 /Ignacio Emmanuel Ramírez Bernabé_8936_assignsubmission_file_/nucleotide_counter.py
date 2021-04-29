"""

NAME
        nucleotide_counter.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/nucleotide_counter.py

DESCRIPTION
        This program calculates the number of DNA bases in a sequence

CATEGORY
        DNA
        Nucleotides

USAGE
        python nucleotide_counter.py

ARGUMENTS


EXAMPLES
        Example 1: Write the sequence 'CATATTGTAGCCCGAAGATTG' as input when the message
        "Escribe tu secuencia de DNA: " has been printed on the screen

        Usage: $ python nucleotide_counter.py

        Input:
        CATATTGTAGCCCGAAGATTG

        Output:
        Escribe tu secuencia de DNA: CATATTGTAGCCCGAAGATTG
        A: 6, C: 4, G: 5, T: 6

"""
# Solicitar la secuencia de DNA al usuario
dna_seq = input('Escribe tu secuencia de DNA: ')

# Obtener la cantidad de cada nucleotido
a_content = dna_seq.count('A')
c_content = dna_seq.count('C')
g_content = dna_seq.count('G')
t_content = dna_seq.count('T')

# Imprimir la cantidad de cada nucleotido
print(f'A: {a_content}, C: {c_content}, G: {g_content}, T: {t_content}')
