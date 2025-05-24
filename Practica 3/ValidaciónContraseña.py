import re

while True:
    try:
        contraseña = input("Ingresa una contraseña (o escribe 'salir'): ")
        if contraseña.lower() == "salir":
            break
        
        if len(contraseña) < 10:
            print("Contraseña demasiado corta")
        elif not any(char.isdigit() for char in contraseña):
            print("Debe agregar al menos un número")
        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
            print("Debe contener al menos un carácter especial")
        else:
            print("Contraseña correcta")
    
    except Exception as e:
        print(f"Ocurrió un error: {e}")
