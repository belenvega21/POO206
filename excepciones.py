try:
    numero = int(input ("Introduce un número: "))
resultado = 10 / numero

print("Resultado:", resultado)

excep valueError:
    print("Error: Se ingreso algo que no es un numero.")
excep ZeroDivisionError:
    print("Error: Estas intentando dividir entre 0")
    