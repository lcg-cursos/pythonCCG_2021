import random

jugar_de_nuevo = "si"
count = 0

while jugar_de_nuevo == "si" and count < 2:

    # Elegir la opcion del usuario
    print("Elige tu opción (piedra, papel o tijera):")
    usuario = input()

    # Definir las posibilidades
    posibilidades = ["piedra", "papel", "tijera"]

    # Elegir la opción de la computadora
    computadora = random.choice(posibilidades)

    print(f"El usuario eligio: {usuario} \nLa computadora eligio: {computadora}")

    # Ejecutar las reglas del juego
    if usuario == computadora:
        print("Es un empate")
    elif usuario == "piedra":
        if computadora == "papel":
            print("Papel gana a piedra: ¡Gana la computadora!")
        else:
            print("Piedra gana a tijera: ¡Tú ganas!")
    elif usuario == "papel":
        if computadora == "tijera":
            print("Tijera gana a papel: ¡Gana la computadora!")
        else:
            print("Papel gana a roca: ¡Tú ganas!")
    elif usuario == "tijera":
        if computadora == "piedra":
            print("Piedra gana a tijera: ¡Gana la computadora")
        else:
            print("Papel gana a tijera: ¡Tú ganas!")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no)")
    count += 1







