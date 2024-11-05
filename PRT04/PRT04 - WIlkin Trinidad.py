
#PRT04 - Wilkin Trinidad 24-0122

class asignatura:
    def __init__(self, Nombre="", Creditos=0, Calificacion=0):
        self.Nombre = Nombre
        self.Creditos = Creditos
        self.Calificacion = Calificacion
        self.Literal = ""
        
        if Calificacion >= 90:
            self.Literal = "A"
        elif Calificacion >= 80:
            self.Literal = "B"
        elif Calificacion >= 70:
            self.Literal = "C"
        elif Calificacion >= 60:
            self.Literal = "D"
        else:
            self.Literal = "F"
    def crear_lista(self, lista:tuple):


        #creo un diccionario solo de las materias y su literiañ
        self.asignaturas = {}

        #agrego los datos a la lista y al diccionario
        for elementos in lista:
                new_asignatura = asignatura(Nombre = elementos[0], Creditos = elementos[1], Calificacion = elementos[2])

                self.asignaturas[new_asignatura.Nombre] = new_asignatura

    def filtrar_asignaturas(self, literal):

        #en esta lista, guardamos un diccionario de los elementos guardados, escribimos [1] para poder acceder a los objetos tipo asignatura
        lista = dict(filter(lambda x:x[1].Literal == literal, self.asignaturas.items()))
        

        #la n es una tupla, ya que son dos elementos, por lo tanto debemos ingresar a su segundo elemento, que es el objeto asignatura :D, soy un montro

        print(f"\n--------------asignaturas con la literal: {literal}--------------")
        for n in lista.items():
            print(f"Nombre: {n[1].Nombre} \nCreditos: {n[1].Creditos} \n")


    def calcular_indice(self):
        #el indice final
        Indice = 0
        #guadamos la cantidad de creditos totales
        creditos_totales = 0
        #guardamos la cantidad de indices por creditos totales
        indice_credito = 0

        #asignamos los valores por los creditos correspondientes
        for item in self.asignaturas.items():
            if item[1].Literal == 'A':
                indice_credito += 4 * item[1].Creditos
            elif item[1].Literal == 'B':
                indice_credito += 3 * item[1].Creditos
            elif item[1].Literal == 'C':
                indice_credito += 2 * item[1].Creditos
            elif item[1].Literal == 'D':
                indice_credito += 1 * item[1].Creditos

            creditos_totales += item[1].Creditos
            
        indice_credito /= creditos_totales

        print(f"\n Tu indice academico es de: {round(indice_credito,2)}")

    def mostrar_informacion(self):
        print(f"Asignatura: {self.Nombre}\n calificacion: {self.Calificacion}\n Literal: {self.Literal}\n Creditos:{self.Creditos}")
    
    def mostrar_asignaturas(self):
        print("\n-------------------Estas son todas tus asignaturas----------------------------")
        for item in self.asignaturas.items():
            item[1].mostrar_informacion()
            print() # <------ salto de linea para hacerlo mas astetic

class persona:
    def __init__(self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad
    def def_mostrar_infomacion(self):
        print(f"hola mi nombre es {self.nombre} y mi edad es : {self.edad} \n")

class Estudiante(persona):

    def __init__(self, nombre = '', edad = 0, matricula=""):
        super().__init__(nombre, edad)
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    #aqui mostraremos la informacion del estudiante
    def def_mostrar_infomacion(self):
        print("\n--------------Estos son los datos personales del estudiante----------------------------")
        super().def_mostrar_infomacion()
        print(f"mi matricula es {self.matricula}")






Local_asignaturas = [

    ("Laboratorio de Física General II", 1, 74),
    ("Adm. Del Procesamiento Electrónico De Datos", 3, 92),
    ("Sistemas Operativos Para Computadoras", 3, 84),
    ("Principios de Ingeniería Eléctrica", 3, 94),
    ("Diseño e Instalación de Redes", 3, 82),
    ("Inglés Técnico I", 3, 87),
    ("Investigación de Operaciones I", 3, 88)
]

 
try:

#---------------iniciamos con el programa--------------------

    print("hola, ingresa los datos del estudiante")

#------------------ingresamos los datos-----------------------

    nuevo_estudiante = Estudiante()
    nuevo_estudiante.nombre = input("ingresa tu nombre: ")
    nuevo_estudiante.edad = int(input("ingresa tu edad: "))
    nuevo_estudiante.matricula = input("ingresa tu matrica: ")
    Literal = input("Ingresa La calificacion literal de la cual quieras filtrar: ").upper()

#-------------------Creamos el objeto asignatura---------------------------
    matematica = asignatura()
    matematica.crear_lista(Local_asignaturas)


    nuevo_estudiante.def_mostrar_infomacion()

    print()



    matematica.filtrar_asignaturas(Literal)


    print()



    matematica.mostrar_asignaturas()

    print()


    matematica.calcular_indice()


    


except:
    print("algo salio mal con la introduccion de los datos")
