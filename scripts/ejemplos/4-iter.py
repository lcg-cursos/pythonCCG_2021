numbers = [2, 4, 6] # Variable iterable
iterador = iter(numbers) # Objeto Iterador

next(numbers)
next(iterador)

numbers = [2, 4, 6]
squares = [n**2 for n in numbers]

squares = (n**2 for n in numbers)
squares

numbers = [2, 4, 6] # Variable iterable
e = enumerate(numbers)
next(e)
list(enumerate(numbers))

numbers = [2, 4, 6] # Variable iterable
for i, num  in enumerate(numbers):
    print(i," valor: ", num)
