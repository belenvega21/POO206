from re import I


try:
    numero = int (input ("Ingres un numero entero positivo mayor que 10: "))
    if numero <= 10:
        raise ValueError ("El numero ingresado no es valido, debe ser mayor quer 10: ")
    
    impares = [str(i) for i in range (2, numero + 1) if I % 2 != 0]
    print ("Número impar ", ", ".join (impares))
     
except ValueError as ve:
    print("Error: De numero ")
except ValueError as e:
    print("Error inesperado: ", e)