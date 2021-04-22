'''
Ruta del archivo de texto: pythonCCG_2021/data/dna.txt
Ruta del programa: pythonCCG_2021/scripts/ejemplos/open.py
'''

# Para correr este programa es important darle la ruta simboloica "../../data/dna.txt"
dna = open("data/dna.txt")
# dna = open("data/dna") # correr esto en consola interactiva

# Leer el archivo
mi_contenido = dna.read()
mi_contenido

print(mi_contenido, "\nlongitud:", len(mi_contenido))
