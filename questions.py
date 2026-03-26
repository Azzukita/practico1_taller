import random
categorias = {
    "Programacion" : ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Cuadros" : ["nacional", "gimnasia", "independiente", "sarmiento", "boca", "river", "brown"],
    "Flores" : ["rosa", "tulipan", "margarita", "orquidea", "jazmin", "lavanda", "girasol", "clavel"]
}

print("¡Bienvenido al Ahorcado!")
print("Categorías disponibles:")
nombres_categorias = list(categorias.keys())
for i, cat in enumerate(nombres_categorias, start=1):
    print(f"  {i}. {cat}")  # ← muestra el número junto al nombre
print()

eleccion = input("Elegí una categoría (número): ")
categorias = list(categorias.keys())

if eleccion == "1":
    categoria_elegida = categorias[0]
elif eleccion == "2":
    categoria_elegida = categorias[1]
elif eleccion == "3":
    categoria_elegida = categorias[2]
else:
    print("Opción no válida, se elige programación por defecto.")
    categoria_elegida = categorias[0]

word = random.choice(categorias[categoria_elegida])
print(f"Categoría elegida: {categoria_elegida}")
print()

guessed = []
attempts = 6
puntos = 0
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntos += 6
        print("¡Ganaste!")
        print (f"puntaje final: {puntos}")
        break
    elif "_" in progress:
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")
        if len(letter) == 1 and letter.isalpha(): 
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntos -= 1
                print("Esa letra no está en la palabra.")
                print()
        else:
            print ("entrada no válida")        
else:
    puntos = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Puntaje final: {puntos}")