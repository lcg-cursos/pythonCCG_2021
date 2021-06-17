# Variables
dna = "AATGATGAACGAC"
bases = ['A','T','G','C']
all_counts = {}

# Creating dinucleotides and counting
for base1 in bases:
    for base2 in bases:
        dinucleotide = base1 + base2
        count = dna.count(dinucleotide)
        if count > 0:
            all_counts[dinucleotide] = count


for dinucleotide, count in all_counts.items():
    if dinucleotide == 'AT':
        print(count)