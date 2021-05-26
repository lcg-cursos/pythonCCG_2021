import argparse
# Create the parser
parser = argparse.ArgumentParser()
# Add the arguments
parser.add_argument("-i", "--input",
                    metavar="path/to/file",
                    help="File with gene sequences",
                    required=True)
# Add optional arguments
parser.add_argument("-o", "--output",
                    help="Path for the output file")
# Add an argument and change it to numeric
parser.add_argument("-int", "--integrer",
                    help="Number of digits to round",
                    type=int,
                    required=False
)
# Execute the parse_args() method
args = parser.parse_args()
# Print arguments
print(args.input, args.output, args.integrer)