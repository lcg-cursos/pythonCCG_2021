'''
## NAME:
  arguments_at.py
## LANGUAGE & VERSION:
  python 3.9.2
## AUTHOR:
  Phabel Antonio López Delgado <phabel2001@gmail.com>
## DATE:
  May, 23rd 2021.
## DESCRIPTION & LOGIC:
  This script opens a file with DNA sequences per line
  and crates a new file with de AT content per line.
  It manages errors with try-except: IOError and N-content
  error. It is meant to be called from commands line
  from terminal with two arguments.
## USAGE:
  arguments_at.py python 3.9.2
## ARGUMENTS:
  -i, --input: file with DNA sequences
  -o, --output: output file with AT content per line.
## INPUT - OUTPUT:
  -i 4_dna_sequences.txt
  -o output_at.txt

## FUNCTIONS:
   No specific functions were defined.
    
## EXAMPLES
  $: python3 arguments_at.py -i 4_dna_sequences.txt -o output_at.txt
  -> Output: output.txt
## SOFTWARE REQUIREMENTS:
  Libraries: argparse
    
## EXTRA COMMENTS:
  Script must be called from command line. If there is a sequence
  with 'N', it will display an error. Take in count try-except structures.
## LAST MODIFICATION:
  Phabel Antonio López Delgado - May 23rd, 2021.
## SOURCE:
  GitHub: https://github.com/phabel-LD/python_class/blob/master/Tasks/arguments_at.py
'''

####################
# Libraries
####################

import argparse

####################
# Define error class
####################

class N_error():
    pass

####################
# Define function
####################

## Pass only the DNA sequence.
def at_content(dna):
    dna = dna.replace(' ', '')
    dna = dna.replace('\"', '')
    dna = dna.replace('-', '')
    dna = dna.upper()
    try: 
        if (dna.count('N') > 0):
            print('N are not valid.')
            raise N_error()
        at_content = (dna.count('A') + dna.count('T'))/len(dna)
        return at_content
    except N_error:
        print(f'Sequence contains {dna.count("N")} N. Not allowed.\n')

####################
# Main code
####################

## Define arguments and parser
parser = argparse.ArgumentParser(description = "This script calculates AT content from files")

parser.add_argument("-i", "--input",
                    help = "File with sequences.",
                    required = True)

parser.add_argument("-o", "--output",
                    help = "File with AT contents.",
                    required = True)

## Execute parse_args(),use args.[arg name]
args = parser.parse_args()

## Get paths
input_path = args.input
output_path = args.output

## Open file
try:
    input_file = open(input_path, 'r')
    data = input_file.readlines()
    input_file.close()
except IOError:
    print('Could not find file.\n')
    input_path = input('Enter valid file: ')
    input_file = open(input_path, 'r')
    data = input_file.readlines()
    input_file.close()

## Open output file.
output_file = open(output_path, 'w')

## Get AT content for every sequence in the input file.
for sequence in data:
    line = sequence.split("=")
    output_file.write(f'AT content for sequence {line[1]} is {at_content(line[1])}\n')
