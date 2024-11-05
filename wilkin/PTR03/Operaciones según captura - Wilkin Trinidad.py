#Wilkin Trinidad - 24-0122

def minuscula(lista:list):
    print("minuscula")
    resultado = 0

    for n in lista:
        resultado += n

    print(f"la suma de {lista} es de {resultado}")

def mayuscula(lista:list):
    print("mayuscula")

    divisibles = list(filter(lambda x: x % 5 == 0, lista))
    resultado = 0
    for n in divisibles:
        resultado += n

    print(f"numeros divisibles entre 5: {divisibles}")
    print(f"la suma entre ellos es: {resultado}")

def numero_caracter(a,b,c):
   
   resultado = (a * b)/c
   print(f"el resultado de  ({a} * {b})/{c} : {resultado}")



try :

    opcion = input("Ingresa un valor: ")

    if opcion == opcion.lower() and opcion.isalpha():
        print("Ingresaste una letra minuscula, Capturando 4 numeros: ")

        
        entradas = []
        while len(entradas) < 4:
         
         entradas.append(int(input("Ingrese un numero: ")))
            
        minuscula(entradas)
    
    elif opcion == opcion.upper() and opcion.isalpha():
        print("Seleccionando una letra mayuscula, Capturando numeros mayores a 15")

        entradas = []

        while len(entradas) < 8:
            dato = int(input("Ingresa un numero menor a 15: "))

            if dato < 15:
                print("Ingresaste un menor a 15, no se tomara en cuenta")
                continue

            entradas.append(dato)
        mayuscula(entradas)

    else:
        print("Seleccionaste un caracter o un numero. Capturando 3 numeros")

        a = int(int(input("Ingrese el numero 01: ")))
        b = int(int(input("Ingrese el numero 02: ")))
        c = int(int(input("Ingrese el numero 03: ")))

        numero_caracter(a=a,b=b,c=c)

except:
    print("Algo salio mal")
