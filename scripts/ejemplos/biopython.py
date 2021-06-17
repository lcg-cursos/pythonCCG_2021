from Bio.Seq import Seq
from Bio.SeqUtils import GC

dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print('Objeto tipo\n', type(dna))

print("3'", dna, "5'")
print("  ", "|" * len(dna))

print("5'", dna.complement(), "3'")  # dna[::-1]
print("3'", dna.reverse_complement(), "5'")
print('Contenido GC: ', GC(dna))

rna = dna.transcribe()
print('Objeto tipo\n', type(rna))
print("RNA: \n3'", rna, "5'")
print("  ", "|" * len(rna))
print("5'", rna.reverse_complement_rna(), "5'")

protein = dna.translate(to_stop=True)
print("Proteina:\n", protein)

