"""
## NAME
    start_position.py

## VERSION

    [0.0]

## AUTHOR

    Zara Paulina Martinez Sanchez <zaram042001@gmail.com

## DATE

    14/04/2021

## DESCRIPTION

    Dada una secuencia de DNA el programa imprime la posición del codón de 
    inicio AUG y la última posición del codón de paro (UAA), así como la 
    secuencia que se transcribe dada en DNA.

## CATEGORY

    Sequence analysis

## USAGE

    start_position.py no cuenta con más opciones

## ARGUMENTS

    No hay argumentos.

## EXAMPLES
    Input:
        Secuencia de DNA a analizar "AAGGTACGTCGCGCGTTATTAGCCTAAT"
    Output:
        El codón de inicio empieza en la posición 4
        El codón de paro termina en la posición 26
        El fragmento que se transcribe (en DNA) es: TACGTCGCGCGTTATTAGCC

"""

dna_sec = "AAGGTACTAAGTCGCGCGTTATTAGCCTAAT"

# Encontrar las posiciones de los codones dentro de la secuencia
inicio = dna_sec.find("TAC")
final = dna_sec.find("TAA")

# Obtener la secuencia que se transcribe con base en los codones encontrados
transcrito = dna_sec[inicio:final]
print("El codón de inicio empieza en la posición " + str(inicio))
print("El codón de paro termina en la posición " + str(final + 2))
print("El fragmento que se transcribe (en DNA) es: " + str(transcrito))
