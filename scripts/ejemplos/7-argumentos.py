import argparse
# Create the parser
parser = argparse.ArgumentParser(description="Programa que obtiene el contenido de AT del archivo de entrada")
# Add the arguments
parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="Archivo con secuencias de genes",
                    required=True)
# Add optional arguments
parser.add_argument("-o", "--output",
                    help="Ruta que tendra el archivo de salida",
                    required=False)
# Add an argument and change it to numeric
parser.add_argument("-r", "--round",
                    help="Número a utilizar al redondear",
                    type=int,
                    required=False
)
# Execute the parse_args() method
args = parser.parse_args()
# Print arguments
print(args.input, args.output, args.round)