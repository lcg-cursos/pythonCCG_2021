"""
NAME 
  tarea_6_drosophila.py

VERSION
  1.0

AUTHOR
  Pablo Sicilia Andrade  <psicilia@gmail.com>


DESCRIPTION
  imprime listas de genes que cumplan condiciones con base en un archivo

CATEGORY
  analisis de secuencia y enlistado

USAGE
  tarea_6_drosophila.py

    
INPUT
  docs/6-data.csv
    
OUTPUT
  none
    
EXAMPLES
input file content:
  Drosophila melanogaster,atatatatatcgcgtatatatacgactatatgcattaattatagcatatcgatatatatatcgatattatatcgcattatacgcgcgtaattatatcgcgtaattacga,kdy647,264
  Drosophila melanogaster,actgtgacgtgtactgtacgactatcgatacgtagtactgatcgctactgtaatgcatccatgctgacgtatctaagt,jdg766,185
  Drosophila simulans,atcgatcatgtcgatcgatgatgcatccgactatcgtcgatcgtgatcgatcgatcgatcatcgatcgatgtcgatcatgtcgatatcgt,kdy533,485
  Drosophila yakuba,cgcgcgctcgcgcatacggcctaatgcgcgcgctagcgatgc,hdt739,85
  Drosophila ananassae,ttacgatcgatcgatcgatcgatcgtcgatcgtcgatgctacatcgatcatcatcggattagtcacatcgatcgatcatcgactgatcgtcgatcgtagatgctgacatcgatagca,hdu045,356
  Drosophila ananassae,gcatcgatcgatcgcggcgcatcgatcgcgatcatcgatcatacgcgtcatatctatacgtcactgccgcgcgtatctacgcgatgactagctagact,teg436,222
output:
nombre   contenido de AT
kdy647   alto
jdg766   medio
kdy533   medio
hdt739   bajo
hdu045   medio
teg436   medio


GITHUB
    https://github.com/psicilia/python_Class/blob/99b9bd1810a3ac2055800201a397fd3fe04bf28e/src/tarea_6_drosophila.py

"""
# Abir archivo
file = open("docs/6-data.csv")
# Leer todas las lineas y guardarlas en una lista
all_lines = file.readlines()
# Cerrar archivo
file.close()

#imprimimos la descricion de la condicion
print('genes pertenecientes a Drosophila melanogaster o a Drosophila simulans')
for line in all_lines:
    line_content = line.split(',')   
    #recorremos todas las lineas y separamos su contendo en una lista, separado por comas
    if line.startswith('Drosophila melanogaster') or line.startswith('Drosophila simulans'):
      #si se el gene pertenece a Drosophila melanogaster o a Drosophila simulans imprimimos el nombre del gen
      print(line_content[2])

#imprimimos la descricion de la condicion
print('genes con una longitud de 90PB  a 110PB')
for line in all_lines:
    line_content = line.split(',')   
    #recorremos todas las lineas y separamos su contendo en una lista, separado por comas
    length = len(line_content[1])
    if (length <= 110) and (length >= 90):
      #imprimimos el nombre del gene si su longitud esta entre 90 y 110 pares de bases 
      print(line_content[2])

#imprimimos la descricion de la condicion
print('genes con AT menor a 50% y expresion mayor a 200')
for line in all_lines:
    line_content = line.split(',')
     #recorremos todas las lineas y separamos su contendo en una lista, separado por comas
    length = len(line_content[1])
    at_content = line_content[1].count('a') + line_content[1].count('t')
    at_percentage = at_content/length
    #calculamos el porcentaje de at
    if at_percentage < 0.5 and int(line_content[3]) > 200:
      # si el porcentaje de at es menor a 50 y la expresion es mayor a 200 imprimimos el nombre del gene
      print(line_content[2]) 

print('genes que inician en K o en H que no son de Drosophila melanogaster')
#imprimimos la descricion de la condicion
for line in all_lines:
    line_content = line.split(',')
     #recorremos todas las lineas y separamos su contendo en una lista, separado por comas
    if (not line.startswith('Drosophila melanogaster') and (line_content[2].startswith('h') or line_content[2].startswith('k'))):
      # si el gene no es de melanogaster e inicia con h o k, imprimimos el nombre del gene
      print(line_content[2]) 

print('nombre \t contenido de AT')
#imprimimos la descricion de la condicion
for line in all_lines:
    line_content = line.split(',')
    #recorremos todas las lineas y separamos su contendo en una lista, separado por comas
    length = len(line_content[1])
    at_content = line_content[1].count('a') + line_content[1].count('t')
    at_percentage = at_content/length
    #calculamos el porcentaje de at
    if at_percentage < .45:
      print(line_content[2] + '\t bajo') #rango de 0% a 45% sin incluir al 45
    elif at_percentage > .65:
      print(line_content[2] + '\t alto')#rango de 65% a 100% sin incluir al 65
    else:
      print(line_content[2] + '\t medio')#rango de 45% a 65%