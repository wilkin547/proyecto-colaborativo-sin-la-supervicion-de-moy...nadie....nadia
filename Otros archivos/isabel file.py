# Captura de datos para analisis
texto = input("Favor introducir un texto(debe contener espacios): ")

#guardamos los resultados en este diccionario
resultados = {}

def Contador_palabras(texto):
    # Para dividir el texto por palabras tomando en cuenta los espacios
    palabras = texto.split()
    # Cuenta la cantidad de palabras
    cantidad_palabras = len(palabras)

    resultados["total de palabras: "] = len(palabras)
    return palabras, cantidad_palabras



def Palabra_mas_larga(palabras):
    return max(palabras, key = len) # Contar en base a la longitud de  la palabra

def Palabras_unicas(palabras):
    return set(palabras) # El set solo admite palabras sin repetir

def Contar_frecuencia(palabras):  
    # Crear tupla vacia
    frecuencia = {}  
    
    for palabra in palabras:  
        if palabra in frecuencia:  
            frecuencia[palabra] += 1  
        else:  
            frecuencia[palabra] = 1  
    
    return list(frecuencia.items()) 

# Imprimir resultados  
def Imprimir_resultados(cantidad_palabras, palabra_larga, unicas, frecuencia_palabras):  
    print("---------- DETALLE ANÁLISIS ----------")  
    print(f"Total de palabras: {cantidad_palabras}")  
    print(f"Palabra más larga: '{palabra_larga}'")  
    print(f"Palabras únicas sin repetir: {unicas}")  
    # Imprimir la lista de tuplas  
    print(f"Lista de tuplas con cada palabra y frecuencia: [{', '.join(str(item) for item in frecuencia_palabras)}]")  #El join las concatena con el paraetro dado(en esto caso una ,)

# Procesar el texto  
palabras, cantidad_palabras = Contador_palabras(texto)  
palabra_larga = Palabra_mas_larga(palabras)  
unicas = Palabras_unicas(palabras)  
frecuencia_palabras = Contar_frecuencia(palabras)  

# Imprimir resultados  
Imprimir_resultados(cantidad_palabras, palabra_larga, unicas, frecuencia_palabras)  