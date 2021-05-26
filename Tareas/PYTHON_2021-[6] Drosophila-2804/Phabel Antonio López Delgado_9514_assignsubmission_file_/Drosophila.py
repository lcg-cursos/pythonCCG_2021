'''
## NAME:
  Drosophila.py

## LANGUAGE & VERSION:
  python 3.9.2

## AUTHOR:
  Phabel Antonio López Delgado <phabel2001@gmail.com>

## DATE:
  May 17, 2021.

## DESCRIPTION & LOGIC:
  This program takes a csv with specific gene data and
  returns gene names corresponding to certain requests.

## USAGE:
  Drosophila.py python3  3.9.2

## ARGUMENTS:
  No specific arguments

## INPUT - OUTPUT:
    Input: file.cvs
    Output: gene lists
    
## EXAMPLES
  Input: 6-data.csv

  Output: (First part):
      Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:
      kdy647
      dg766
      kdy533

## SOFTWARE REQUIREMENTS:
  This script runs in python3 3.9.2
    
## EXTRA COMMENTS:

## LAST MODIFICATION:
  Phabel Antonio López Delgado - May 17, 2021 [Creation]

## SOURCE:
  GitHub: https://github.com/phabel-LD/python_class/blob/master/Tasks/Drosophila.py
'''

## Imprimir los genes  pertenecientes a *D. melanogaster* o *D. simulans*.
data_file = open("6-data.csv", "r")
print("Genes que pertenecen a Drosophila melanogaster o Drosophila simulans:")
for line in data_file:
    data_list = line.split(',')
    # Seleccionar genes de organismo adecuado.
    if (data_list[0] == "Drosophila melanogaster" or data_list[0] == "Drosophila simulans"):
        print(data_list[2])

## Imprimir los genes de entre 90 y 110 bases de longitud.
data_file = open("6-data.csv", "r")
print("\nGenes de entre 90 y 110 bases de longitud:")
for line in data_file:
    data_list = line.split(',')
    # Establecer criterios de longitud.
    if (len(data_list[1]) > 90 and len(data_list[1]) < 110):
        print(data_list[2])

## Imprimir los genes con contenido de AT < a 0.5 y nivel de expresión > 200.
data_file = open("6-data.csv", "r")
print("\nGenes con contenido de AT < a 0.5 y nivel de expresión > 200:")
for line in data_file:
    data_list = line.split(',')
    # Calcular contenido AT
    at_content = 0
    for nucleotide in data_list[1]:
        if (nucleotide == "a" or nucleotide == "t"):
            at_content += 1
    at_content = at_content/len(data_list[1])
    # Contenido de AT y expresion correctos.
    if (at_content < 0.5 and int(data_list[3]) > 200):
        print(data_list[2])

## Imprimir los genes que inicien con "k" o "h", evitar D. melanogaster.
data_file = open("6-data.csv", "r")
print("\nGenes que inicien con 'k' o 'h', evitar D. melanogaster:")
for line in data_file:
    data_list = line.split(',')
    # Usar el metodo str.startswith()
    if(data_list[2].startswith("k") or data_list[2].startswith("h")) and (data_list[0] != "Drosophila melanogaster"):
        print(data_list[2])

## Para cada gen, dar nombre, y tipo de at_content
data_file = open("6-data.csv", "r")
print("\nGenes y contenido AT:")
for line in data_file:
    data_list = line.split(',')
    at_content = 0
    # Calcular contenido de AT
    for nucleotide in data_list[1]:
        if nucleotide == "a" or nucleotide == "t":
            at_content += 1
    at_content = at_content/len(data_list[1])
    # Pasar por las tres diferentes opciones.
    if(at_content > 0.65):
        print(data_list[2] + " tiene contenido de AT alto.")
    elif(at_content < 0.45):
        print(data_list[2] + " tiene contenido de AT bajo.")
    else:
        print(data_list[2] + " tiene contenido de AT medio.")
        
data_file.close()
