try:
    frase = input("Ingresa una frase: ").strip()
    letra = input("Ingresa una letra: ").strip()

    if not frase:
        raise ValueError("La frase no puede estar vacía.")
    if any(char.isdigit() for char in frase):
        raise ValueError("La frase no debe contener números.")
    if len(letra) != 1 or not letra.isalpha():
        raise ValueError("Debes ingresar una sola letra válida.")

    conteo = frase.lower().count(letra.lower())
    print(f"La letra '{letra}' aparece {conteo} veces en la frase.")

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Error inesperado:", e)
