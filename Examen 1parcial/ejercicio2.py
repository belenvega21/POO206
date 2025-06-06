try:
    palabra1 = input("Introduce la primera palabra: ")
    palabra2 = input("Introduce la segunda palabra: ")

    if len(palabra1) > len(palabra2):
        print(f"{palabra1} es más larga que {palabra2} con {len(palabra1) - len(palabra2)} letras.")
    elif len(palabra2) > len(palabra1):
        print(f"{palabra2} es más larga que {palabra1} con {len(palabra2) - len(palabra1)} letras.")
    else:
        print("Ambas palabras tienen la misma longitud.")
except:
    print("Error: Introduce un valor válido")
print("Fin del programa")

