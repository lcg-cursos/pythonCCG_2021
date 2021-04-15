### Calcula el contenido de AT y GC de una secuencia
my_dna = "ACTGTACGTGCACTGATC"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
g_count = my_dna.count('G')
c_count = my_dna.count('C')

at_content = (a_count + t_count) / length
gc_content = (g_count + c_count) / length

print("AT content is " + str(at_content))
print("GC content is " + str(gc_content))
print("AT + GC sum is: " + str(at_content + gc_content))