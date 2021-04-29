'''
## NAME:
    AUG_position.py

## LANGUAGE & VERSION:
    python [3.9.2]

## AUTHOR:
    Phabel Antonio López Delgado <phabel2001@gmail.com>

## DATE:
    10/abr/2021

## DESCRIPTION & LOGIC:
    Este programa pregunta por una secuencia de DNA, y proporciona las posiciones
    de inicio y termino de la secuencia transcrita, así como dicha secuencia en DNA
    y RNA. Para preguntar por la seq. se usa el procedimiento input() y para
    hallar dichas posiciones .find(). También se hace uso de seleccionar cierto
    rango de una string con string[A:B].

## USAGE:
    AUG_position.py no tiene otrsa especificaciones.

## ARGUMENTS:
    No hay argumentos necesarios.

## INPUT - OUTPUT:
    Input: Una secuencia de Nucleótidos en Mayúsculas.
    Output: Un string que indica posiciones y secuencias DNA y RNA.
    
## EXAMPLES
    Input:
        Introduzca la secuencia a analizar: AAGGTACGTCGCGCGTTATTAGCCTAAT
    Output:
        RNA sequence is: UUCCAUGCAGCGCGCAAUAAUCGGAUUA
        AUG starts at 4 and Stops at 26
        Fragmento de RNA es será transcrito (en DNA): TACGTCGCGCGTTATTAGCC
        
## SOFTWARE REQUIREMENTS:
    No se usaron librerías, únicamente strings y procedimientos de print,
    casting y .find().
    
## EXTRA COMMENTS:
    Esta es el programa-tarea 1.
    
## LAST MODIFICATION:
  Phabel Antonio López Delgado - 10/abr/2021 - Creación del código.

'''

## Preguntar al usuario la seq. de DNA
seq_DNA = input('Introduzca la secuencia a analizar: ')
seq_DNA = seq_DNA.upper() ## Convertir todo a mayúsculas. Es más robusto incluirlo aquí.


## Posicion de AUG-->TAC y STOP: UAA-->TAA
TAC_position = seq_DNA.find("TAC") ## Se usa .find() --> Ubicar inicio.
TAA_position = seq_DNA.find("TAA")+2 ## Ubicar final. Se suman dos elementos para incluir todo el STOPcodon


## Imprimir la cadena completa se tiene...
AUG_position = "El codon TAC empieza en la posición " + str(TAC_position) + " y termina en " + str(TAA_position)
print(AUG_position)


## Fragmento de DNA que será transcrito
DNA_transcripted = "Fragmento de RNA es será transcrito (en DNA): " + str(seq_DNA[TAC_position:TAA_position-2])
print(DNA_transcripted)





