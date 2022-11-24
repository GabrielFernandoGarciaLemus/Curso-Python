import pickle

class Persona:
    def __init__(self, nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo= sexo
        
    def datosPersonales(self):
        print("El nombre de la persona es: ", self.nombre)
        print("La edad de la persona es: ", self.edad)
        print("El sexo de la persona es: ", self.sexo)
        
        
miPersona1 = Persona("Gabriel",20,"Masculino")
miPersona2 = Persona("Gustavo", 21,"Masculino")
miPersona3 = Persona("Marisol",49,"Femenino")



listaPersonas = [miPersona1,miPersona2,miPersona3]

fichero = open("Personas","wb")

pickle.dump(listaPersonas,fichero)

fichero.close()

del(fichero)

ficheroleer = open("Personas", "rb")
miPersona = pickle.load(ficheroleer)
ficheroleer.close()

for i in miPersona:
    print(i.datosPersonales())
    