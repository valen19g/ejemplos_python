#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  questions.py
#  
#  Copyright 2026 Usuario <Usuario@DESKTOP-CVT50SA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import random
words = [
"python",
"programa",
"variable",
"funcion",
"bucle",
"cadena",
"entero",
"lista",
]
word = random.choice(words)
guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
progress = ""
for letter in word:
if letter in guessed:
progress += letter + " "
else:
progress += "_ "
print(progress)# Verificar si el jugador ya adivinó la palabra completa
if "_" not in progress:
print("¡Ganaste!")
break
print(f"Intentos restantes: {attempts}")
print(f"Letras usadas: {', '.join(guessed)}")
letter = input("Ingresá una letra: ")
if letter in guessed:
print("Ya usaste esa letra.")
elif letter in word:
guessed.append(letter)
print("¡Bien! Esa letra está en la palabra.")
else:
guessed.append(letter)
attempts -= 1
print("Esa letra no está en la palabra.")
print()
else:
print(f"¡Perdiste! La palabra era: {word}")
