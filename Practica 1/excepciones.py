try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")
