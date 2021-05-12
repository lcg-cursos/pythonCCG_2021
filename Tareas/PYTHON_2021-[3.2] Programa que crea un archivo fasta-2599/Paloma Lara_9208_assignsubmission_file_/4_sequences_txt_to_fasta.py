'''
NAME
       secuencias_txt_a_fasta

VERSION
       1.0

AUTHOR
       Paloma Lara <palomalf86@gmail.com>

DESCRIPTION
       Genera un archivo fasta con base en un archivo txt en el siguiente
       formato seq_1 = ATG..

CATEGORY
       

USAGE
       program [OPTIONS]

ARGUMENTS

SOFTWARE REQUERIMENTS

IMPUT
     Requiere como imput un archivo llamado "4_dna_sequences.txt"
     que contenga una o varias lineas en el formato "seq_1 = ATG.."

OUTPUT
     Genera un archivo con todas las secuencias contenidas en
     "4_dna_sequences.txt", ahora en formato fasta

CREATION DATE
     02/05/2021
     
LOCALIZACION EN GIT https://github.com/larafp86/Templates



'''
#abre el archivo con secuencias en formato txt
my_file = open("../docs/ejercicios/4_dna_sequences.txt")
#lee las lineas y las guarda en la variable all_lines
all_lines= my_file.readlines()
#cierra el archivo con secuencias en formato txt
my_file.close
#Crea un nuevo archivo llamado 4_dna_sequences.fasta con el argumento a
#para que agregue 
my_newfile= open("../output/4_dna_sequences.fasta", "a")
#Ciclo for para que linea por linea se modifique el formato a fasta y
#se escriba en el archivo 4_dna_sequences.fasta"
for line in all_lines:
    #quita las comillas
    line_without_qm = line.replace('"',"")
    #encuentra la posicion del signo "="
    position=line_without_qm.find("=")
    #Convierte la lina a formato fasta
    line_fasta=(">" + line_without_qm[:position] + "\n" + line_without_qm[position+2:])
    my_newfile.write(line_fasta)
#Cierra el archivo
my_newfile.close()
#Fin
