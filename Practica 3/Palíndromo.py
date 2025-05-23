try:
    cadena = input("Ingresa una cadena de texto: ")
    if cadena == cadena [::-1]:
        print("La cadena es un Palíndromo")
    else:
        print("La cadena no es un Palíndrono")
except Exception as e:
    print("Ocurrio un error {e}")
    