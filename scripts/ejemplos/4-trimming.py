file = open("data/4_input_adapters.txt")
line = file.readlines()
file.close()

output_file = open("output/trimmed.txt", "w")

for dna in line:
    #print(dna)
    trimmed_dna = dna[14:]
    output_file.write(trimmed_dna)

output_file.close()