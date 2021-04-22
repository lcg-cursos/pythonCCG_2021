'''
- En pyCharm podemos configurar cada script para
que corra en distintos directorios.

- O crear un Template para que se corra siempre
desde el working directory.

Edit configurations... -> Edit templates ->
Templates -> Python -> working directory

'''

# checar la ruta donde me encuentro
import os
print(os.getcwd())
os.chdir("/Users/user/Documents/Doctorado/Courses/Taught/pythonCCG_2021")
print(os.getcwd())