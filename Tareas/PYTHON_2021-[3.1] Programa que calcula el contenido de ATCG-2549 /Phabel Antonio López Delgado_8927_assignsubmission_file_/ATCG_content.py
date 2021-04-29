'''
## NAME:
  ATCG_content.py

## LANGUAGE & VERSION:
  python 3.9.2

## AUTHOR:
  Phabel Antonio Lopez Delgado <phabel2001@gmail.com>

## DATE:
  17/abr/2021

## DESCRIPTION & LOGIC:
  Este programa cuenta la cantidad de cada nucleótido [ATCG] en una cadena de DNA
  proveida como string. Los cuenta individualmente con el metodo .count('[NT]')
  e imprime el resultado con la etiqueta correspondiente.

## USAGE:
  El uso es bioinformático, corre en Python. 

## ARGUMENTS:
  No requiere argumentos.

## INPUT - OUTPUT:
  INPUT es una secuencia tomada como string de Nucleótidos [ATCG]
  OUTPUT es un mensaje con el numbre de cada nucleótido y su conteo dentro de la
  secuencia.
    
## EXAMPLES
  Ingrese secuencia (solo introduzca A,C,G,T): AAGGAUGTCGCGCGTTATTAGCCTAA
  A: 7, C: 5, G: 7, T: 6

## SOFTWARE REQUIREMENTS:
  El programa fue elaborado y corre en python 3.9.2. No se requieren librerías
  adicionales.
    
## EXTRA COMMENTS:
  Sin comentarios extra.

## LAST MODIFICATION:
  Creación: Phabel Antonio Lopez Delgado - 17/abr/2021.
    
## GITHUB:
  https://github.com/phabel-LD/python_class/edit/master/Tasks/ATCG_content.py

'''


## Pedir input de secuencia cualquiera
nucleotide_Seq = input('Ingrese secuencia (solo introduzca A,C,G,T): ')

## Contar con los 4 nucleotidos. Usar 1 variable para cada uno.
A_content = nucleotide_Seq.count('A')
C_content = nucleotide_Seq.count('C')
G_content = nucleotide_Seq.count('G')
T_content = nucleotide_Seq.count('T')

## Imprimir los counts ordenadamente: A C G T.
print(f'A: {A_content}, C: {C_content}, G: {G_content}, T: {T_content}')
