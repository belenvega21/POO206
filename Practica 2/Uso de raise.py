def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

try:
    resultado = dividir(10, 0)
    print(resultado)
except ValueError as e:
    print(f"Error capturado: {e}")
    