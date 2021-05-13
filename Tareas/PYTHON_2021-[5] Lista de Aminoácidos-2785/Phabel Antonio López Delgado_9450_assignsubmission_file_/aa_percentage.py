'''
## NAME:
  aa_percentage.py

## LANGUAGE & VERSION:
  python [3.9.2]

## AUTHOR:
  Phabel Antonio López Delgado <phabel2001@gmail.com>

## DATE:
  May 11th, 2021.

## DESCRIPTION & LOGIC:
  This program has a function that returns the percentage of
  a list of aminoacidsto search from another list. It has a
  default search list: hydrophilic aminoacids.

## USAGE:
  aa_percentage.py python3

## ARGUMENTS:
  The function's arguments are a total list to scan and
  a search list. Both of aminoacids.

## INPUT - OUTPUT:
  Input: total_list (the aminoacid list to scan) &
          aa_list (the aminoacids t search)
  Output: A percentage (float rounded to 6 decimals)

    
## EXAMPLES
  Like the assert test:
    Input:
        get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"])
    Output:
        5.0

## SOFTWARE REQUIREMENTS:
  python3
    
## EXTRA COMMENTS:
  The function has a default argument: hydrophilic aminoacids.

## LAST MODIFICATION:
  Phabel Antonio López Delgado   May 11th, 2021.

## SOURCE:
  GitHub: https://github.com/phabel-LD/python_class/blob/master/Tasks/aa_percentage.py
'''

## Funcion
def get_aa_percentage(total_list, aa_list=['A','I','L','M','F','W','Y','V']):
    total_count = 0
    ## Contar para cada aminoacido a buscar
    for aminoacid in aa_list:
        total_count += total_list.count(aminoacid)
    ## Obtener porcentaje
    aa_percentage = 100*(total_count/len(total_list))
    ## Redondear a 6 decimales
    aa_percentage = round (aa_percentage, 6)
    return(aa_percentage)


## Main code
## Comprobar con tests assert.
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert get_aa_percentage("MSRSLLLRFLLFLLLLPPLP") == 65

## Ingresar lista de aminoacidos.
aminoacids = input('Ingrese lista de aminoacidos totales usando single-letter code: ')
aminoacids = aminoacids.upper()
total_list = list (aminoacids)

## Ingresar lista de aminoacidos a buscar.
req_aminoac = input('Ingrese lista de aminoacidos a buscar usando single-letter code: ')
req_aminoac = req_aminoac.upper()
aa_list = list (req_aminoac)

## Usar valor default si no se tiene aa_list.
if (not aa_list):
    percentage = get_aa_percentage(total_list)
else:
    percentage = get_aa_percentage(total_list, aa_list)
print(percentage)
