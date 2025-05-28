while True:
    try: 
        entrada = input("Introduce un numero entero (escribe 'salir' para terminar): " )
        if entrada.lower() == "salir":
            print("Programa terminado")
            break
        
        numero = int (entrada)
        
        if numero % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")
    except ValueError:
        print("Error: Agrega un número entero. ")
    except Exception as a:
        print(f"Ocurrio un error: {a} ")
    