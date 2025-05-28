try:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero < 0:
        raise ValueError("El número debe ser positivo.")

    cuenta_atras = [str(i) for i in range(numero, -1, -1)]
    print("Cuenta atrás:", ", ".join(cuenta_atras))

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("Error inesperado:", e)