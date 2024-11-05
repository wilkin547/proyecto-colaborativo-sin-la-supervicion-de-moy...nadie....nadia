# Wilkin Trinidad 24-0122

def Fibonacci(numero):
    print("fibobachi \n")

    serie = [0,1]

    #uso esto para quitar los corchetes, por favor nadia, no me quite mas punto que no quiero quemar esta materia :,v
    str_serie = "0, 1"

    while serie[-1] < numero:

        new_number = serie[-1] + serie[-2]


        # debido a como esta escrito la condicion de este bucle, aveces puede pasar la que la serie se pase, asi que le pregunte si el nuevo numero se pasa de la serie y si es asi, que no lo agrege
        if new_number > numero: break

        str_serie += f", {new_number}"
        serie.append(new_number)


    print(f"serie de fibonacci hasta : {numero}")
    print(str_serie)
            

def Factorial(numero):
    print("Factorial \n")

    lista = range(2,numero + 1)
    str_resultado = "1"
    int_resultado = 1

    for n in lista :
        int_resultado *= n
        str_resultado += f" * {n}"

    print(f"El resultado de {numero} factorial es de: ")
    print(f"{str_resultado} = {int_resultado}" )






def Tabla_De_Multiplicar(first, second):
    print("Tabla de multiplicar")




    if second < first:
        print("EL segundo numero es menor que el primero, por fabor ingresa un numero mayor")
        
    else:
        multiplicador = range(1,11)
        multiplicando = range(first, second + 1)

        for F in multiplicando:
            print (f"Tabla de multiplicar del {F}:")
            for S in multiplicador:
                print (f"{F} x {S} = {F * S}")

            #espacio en blanco    
            print()


try :

    opcion = int(input("----Menu----- \n 1. fibonacci \n 2. factorial \n 3. tabla de multiplicar \n 4. salir \n opcion: "))

    if opcion == 1:

        numero = int(input("ingresa un numero"))
        Fibonacci(numero)
    
    elif opcion == 2:

        numero = int(input("ingresa un numero"))
        Factorial(numero)

    elif opcion == 3:
        First = int(input("ingresa un numero: "))
        Second = int(input("ingresa un segundo numero: "))

        Tabla_De_Multiplicar(first=First, second=Second)
    else :
     print("saliste")
except:
    print("algo salio mal")


