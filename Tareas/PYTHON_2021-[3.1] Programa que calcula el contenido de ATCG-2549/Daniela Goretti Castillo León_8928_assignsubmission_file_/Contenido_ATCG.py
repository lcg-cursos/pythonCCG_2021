# Este programa calcula el contenido de las bases 'A', 'C', 'T' y 'G' de una secuencia.
# La liga de Github donde se encuentra el encabezado de este programa es https://github.com/Danigore25/python_class/blob/master/src/Template_Contenido_ATCG
# La liga de Github donde se encuentra este programa es https://github.com/Danigore25/python_class/blob/master/src/Contenido_ATCG.py

print('Por favor escriba la secuencia de DNA: \n') # En esta parte se pide al usuario la secuencia de DNA que se va a analizar.
dna = input() # dna es una variable que guarda la secuencia que escribe el usuario.
cantidad_de_A = (dna.count('A')) # La variable cantidad_de_A cuenta con el método count que permite contar el contenido de 'A' que hay en la secuencia.
cantidad_de_C = (dna.count('C')) # La variable cantidad_de_C usa el método count para contar las 'C' que tiene la secuencia.
cantidad_de_T = (dna.count('T')) # La variable cantidad_de_T calcula el contenido de 'T' que hay en la secuencia.
cantidad_de_G = (dna.count('G')) # La variable cantidad_de_G cuenta las 'G' que se encuentran en la secuencia.

print("Cantidad de A: ",cantidad_de_A,", cantidad de C: ",cantidad_de_C,", cantidad de G: ",cantidad_de_G, ", cantidad de T: ",cantidad_de_T)
# Al final se imprime el contenido de cada base que existe en la secuencia.