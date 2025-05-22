try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error: {e}")