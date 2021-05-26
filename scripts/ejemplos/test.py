def displayText():
    print("Yes! you are importing a function")

class AmbiguousBaseError(Exception):
    '''A new error class object'''
    pass

def get_at_content(dna):
    '''Takes a DNA seq and calculates AT content'''
    if dna.count("N") > 0:
        raise AmbiguousBaseError(f'Sequence contains {dna.count("N")} N\'s')
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

dna = 'ATGCCCTATACGTA'

print(f'Variable __name__: {__name__}')

if (__name__ == '__main__'):
    displayText()
    print(get_at_content(dna))
