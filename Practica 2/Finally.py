try:
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    print("Este bloque se ejecuta siempre.")