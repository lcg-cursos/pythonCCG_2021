print("DNA sequence:")
dna = input()
#dna = "AAAACCCGGT"
rev = dna[::-1]
rev = rev.replace("A","t")
rev = rev.replace("T","a")
rev = rev.replace("C","g")
rev = rev.replace("G","c")

print(rev.upper())
