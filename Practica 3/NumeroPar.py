try: 
    numero = int (input ("Introduce un numero entero:" ))
    if numero % 2 == 0: 
        print ("El número es par. ")
    else:
        print("El numero es impar.")
except ValueError:
    print("Error: Agrega un número entero. ")
    