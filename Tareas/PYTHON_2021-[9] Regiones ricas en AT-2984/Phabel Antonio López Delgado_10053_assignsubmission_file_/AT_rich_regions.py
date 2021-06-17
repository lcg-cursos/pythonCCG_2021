'''
## NAME:
  AT_rich_regions.py
  
## LANGUAGE & VERSION:
  python 3.8.5
  
## AUTHOR:
  Phabel Antonio López Delgado <phabel2001@gmail.com>
  
## DATE:
  June 05th, 2021.
  
## DESCRIPTION & LOGIC:
  This code contains a function, which receives a dna sequence, searchs for
  AT rich (>=5 ATs) regions and raises an error when ambiguous bases are found.
  
## USAGE:
  AT_rich_regions.py python 3.8.5
  
## ARGUMENTS:
  No additional arguments were used.

## INPUT - OUTPUT:
  Input: DNA sequence

  Output: AT-rich regions or error.

## EXAMPLES
  Provide dna sequence (all capitals): CTGCATTATATCGTACGAAATTATACGCGCG
  From the dna sequence CTGCATTATATCGTACGAAATTATACGCGCG.
  AT-rich regions: ['ATTATAT', 'AAATTATA']

## SOFTWARE REQUIREMENTS:
  python3
  libraries: re
  
## FUNCTIONS:

   at_regions(dna):
       [receives a dna sequence, searchs for
        AT rich (>=5 ATs) regions and raises an error
        when ambiguous bases are found. There is no return()]
   
## EXTRA COMMENTS:
   The error raised points out the first ambiguous base.

## LAST MODIFICATION:
  Phabel Antonio López Delgado: June 05th, 2021. [Creation]

## SOURCE:
  GitHub: https://github.com/phabel-LD/python_class/blob/master/Tasks/AT_rich_regions.py
'''

####################
# Import libraries
####################

import re


####################
# Define function
####################

def at_regions(dna_seq = "CTGCATTATATCGTACGAAATTATACGCGCG"):
    ## Define specific error
    class invalid_base(Exception):
        pass

    ## Validate sequence 
    try:
        invalidation = re.search(r"[^ATGC]", dna_seq)
        if invalidation:
            raise invalid_base
        at_rich = re.findall(r'[AT]{5,}', dna_seq)
        print(f'From the dna sequence {dna_seq}.')
        print(f'AT-rich regions: {at_rich}')
    ## Mark an error
    except invalid_base:
        print('Ambiguos base found! Seek solution.')
        print(f'Ambiguous base: {invalidation}')


####################
# Main code
####################

dna = input('Provide dna sequence (all capitals): ')
at_regions(dna)
