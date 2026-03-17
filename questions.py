

import random
categorias ={
"tipos_de_datos" : ["cadena","entero","lista"],
"cosas_de_un_programa": ["bucle","variable","funcion"],
"otros": ["python","programa"]
}

guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
for categoria in categorias:
	print("--", categoria)
choice = input("elegir categoria ").lower()
if choice not in categorias:
	print ("no existe esa categoria se usara otros")
	choice= "otros"
	word = random.choice(categorias[choice])
mezcla = random.sample(categorias[choice], len(categorias[choice]))


puntaje=0
while len(mezcla) > 0:
    word = mezcla.pop()
    guessed = []
    attempts = 6

    while attempts > 0:
        # Mostrar progreso
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            puntaje -= 1
            attempts -= 1
            print("Esa letra no está en la palabra.")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0

    
    print(f"Tu puntaje es {puntaje}")