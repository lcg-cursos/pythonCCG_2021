import argparse

"""

NAME
        4_at_content.py

VERSION
        [1.0]

AUTHOR
        Ignacio Emmanuel Ramirez Bernabe

CONTACT
        iramirez@lcg.unam.mx

GITHUB
        https://github.com/eveiramirez/python_class/blob/master/python_scripts/4_at_content.py

DESCRIPTION
        This program gets the AT content of the sequences of the 4_dna_sequences.txt file

CATEGORY
        DNA
        AT content

USAGE
        python 6_data_genes.py [OPTIONS]

ARGUMENTS
        -h, --help          show this help message and exit
        -i, --input         input file path
        -o, --output        output file path
        -r, --round         number of digits to round

EXAMPLES
        Example 1:  Run the program in the same directory as the 4_dna_sequences.txt file

        Usage: $ python 4_at_content.py -i path_to_file

        Input:
        4_dna_sequences.txt

        Output:
        4_at_content.txt (Default)


"""

# Crear la descripcion del programa
parser = argparse.ArgumentParser(description="Script that calculates the AT content of the sequences in the "
                                             "4_dna_sequences.txt file")

# Anadir los argumentos
parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences")

parser.add_argument("-o", "--output",
                    help="Output file path",
                    default="4_at_content.txt")

parser.add_argument("-r", "--round",
                    help="Number of digits to round",
                    type=int,
                    default=2)


# Crear la excepcion AmbiguousBaseError
class AmbiguousBaseError(Exception):
    pass


# Calcular el contenido de AT
def get_at_content(dna, dec):
    if dna.count("N") > 0:
        raise AmbiguousBaseError(f'Sequence contains {dna.count("N")} N\'s')

    length = len(dna)
    a_content = dna.count('A')
    t_content = dna.count('T')
    at_content = (a_content + t_content) / length

    return round(at_content, dec)


# Obtener las secuencias y su contenido de AT
def get_seqs(fil, outp, arg):
    i = 1

    # Obtener el contenido de AT de cada secuencia
    for line in fil:
        try:
            # Obtener la secuencia de cada linea
            seq = line.split('\"')[1]
            seq = seq.replace('-', '')
            seq = seq.upper()

            # Guardar el resultado de la secuencia
            try:
                outp.write(
                    f"The AT content of the sequence '{seq}' is {(get_at_content(seq, arg.round))}\n")

            # Imprimir un error si contiene N's
            except AmbiguousBaseError as err:
                print(f'Skipping invalid sequence on line {i}: {err.args[0]}')

        # Imprimir si no hay secuencia entre comillas
        except IndexError as err:
            print(f'There is no sequence in quotes on line {i}: ' + err.args[0])
        i += 1


# Preguntar si desea continuar con el proceso
def continue_process():
    try_again = input("Do you want to enter a new path?: [y/n]\n")
    if try_again == "y":
        new_p = input("Enter a path:\n")
        return new_p, 0
    else:
        print("Process finished")
        return None, 1


# Ejecutar el metodo parse_args()
args = parser.parse_args()

# Guarda la direccion del archivo en path
path = args.input
end_process = 0

# Crear el archivo con el contenido de AT
while not end_process:
    # Abrir el archivo y revisar si es valido
    try:
        if path is None:
            raise AmbiguousBaseError("Missing input file")
        elif path.find('4_dna_sequences.txt') == -1:
            raise AmbiguousBaseError("Invalid file: The file is not 4_dna_sequences.txt")
        else:
            with open(path) as file:

                # Crear el archivo de los resultados
                try:
                    with open(args.output, "w") as output_file:

                        # Obtener el contenido de AT de cada secuencia y guardarlo en el archivo final
                        try:
                            get_seqs(file, output_file, args)

                        # Cerrar el archivo con los resultados
                        finally:
                            output_file.close()
                except IOError as ex:
                    print('The output file could not be created: ' + ex.strerror)

                # Cerrar el archivo usado como input
                finally:
                    file.close()
                    # Indicar que la ruta del input ya fue valida
                    end_process = 1

    # Imprimir un error si la ruta del input es invalida y preguntar si continuar con el proceso
    except IOError as ex:
        print('File not found: ' + ex.strerror)
        path, end_process = continue_process()
    except AmbiguousBaseError as ex:
        print(ex.args[0])
        path, end_process = continue_process()
