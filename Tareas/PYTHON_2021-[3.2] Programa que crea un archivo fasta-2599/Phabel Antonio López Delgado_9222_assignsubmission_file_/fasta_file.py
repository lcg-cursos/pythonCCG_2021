
'''
## NAME:
  fasta_file.py
  
## LANGUAGE & VERSION:
  python 3.9.2
  
## AUTHOR:
  Phabel Antonio Lopez Delgado <phabel2001@gmail.com>
  
## DATE:
  April 30th, 2021.
  
## DESCRIPTION & LOGIC:
  This script takes a txt file with NT sequences and creates a fasta file with them.
## USAGE:
  This script is aimed for python3. The main method implemented is: open(), readlines()
## ARGUMENTS:
  No extra arguments needed.
## INPUT - OUTPUT:
  Input: 4_dna_sequences.txt
  Output: dna_sequences.fasta
    
## EXAMPLES
  4_dna_sequences.txt
            seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
            seq_2 = "actgatcgacgatcgatcgatcacgact"
            seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"
            
   dna_sequences.fasta
            >seq_1
            ATCGTACGATCGATCGATCGCTAGACGTATCG
            >seq_2
            ACTGATCGACGATCGATCGATCACGACT
            >seq_3
            ACTGACACTGTACTGTACATGTG
   
## SOFTWARE REQUIREMENTS:
  This script runs with python 3.9.2. No extra libraries were used.
    
## EXTRA COMMENTS:
    The string modifications for the lines will depend on the input file's structure.
    With other input files, other modifications may be needed o not.
## LAST MODIFICATION:
  Phabel Antonio Lopez Delgado: April 30th, 2021.
  
## GITHUB
  https://github.com/phabel-LD/python_class/edit/master/Tasks/fasta_file.py
  
'''

## Abrir archivo como lectura con open("","r+")
data = open("../Listas_y_loops/4_dna_sequences.txt", "r+") ## Recordar comprobar la ruta del archivo input.

lines = data.readlines() ## Leer cada linea.

data.close() ## Cerrar el archivo, pues ya no es necesario.

file = open("dna_sequences.fasta", "w") ## Crear el archivo output.

for line in lines: ## Iterar sobre cada linea y anexar lo necesario al nuevo archivo fasta
    file.write(">" + line[:5] + "\n") ## Escribir encabezado
    line = line.upper() ## Asegurarse que todos los nucleotidos sean mayusculas.
    line = line.replace('-', '') ## Eliminar gaps.
    line = line.replace('"', '') ## Eliminar comillas
    ## print(line)  ## Este es un buen checkpoint para revisar el output
    file.write(line[8:]) ## Escribir la secuencia en otro renglon.

file.close() ## Cerrar el archivo output: fasta
