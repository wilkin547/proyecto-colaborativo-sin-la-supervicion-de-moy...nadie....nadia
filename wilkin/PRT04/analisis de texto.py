


def cantidad_de_palabras():
    resultados["Total de palabras: "] = len(lista)

def palabras_larger():

    #aqui guardamos la palabra mas grande
    biggest = ""

    #si la palabra actual es mayor que el biggest, entones el biggest es igual a esa palabra
    for palabra in lista:
        if len(palabra) > len(biggest):
            biggest = palabra

    resultados["Palabra mas larga :"] = biggest

def palabras_unicas():

    resultados["palabras unicas sin repetir: "] = set(lista)

#aqui guardaremos las tuplas y su lista de resultados 
def tuplas():

    lista_de_tuplas = []
    for palabra in resultados["palabras unicas sin repetir: "]:
            lista_de_tuplas.append((palabra,lista.count(palabra)))
    resultados["Lista de tuplas con cada palabra y su frecuencia"] = lista_de_tuplas

try:
    #aqui guardamos el texto por el usuario
    texto = input("ingresa un texto cualquiera: ")
    #aqui guarmos la listas de palabras dividida entre espacios
    lista = texto.split(" ")
    #aqui guardamos los resultados
    resultados = {}


    print("---------------DETALLE ANALISIS ---------------")
    cantidad_de_palabras()
    palabras_larger()
    palabras_unicas()
    tuplas()

    for elementos in resultados.items():
        print(elementos[0],elementos[1])

except:
    print("algo salio mal con el codigo")

