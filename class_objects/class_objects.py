## Class: type of object that we can create - properties 
## We use snake case in python - separete words with underscore
class CelularStaticAtributes():
    # Static attributes - they are same for all
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"

#Creating instance
celular1 = CelularStaticAtributes()
print(celular1.marca)

class Celular:
    # This method is executed automatically when we create an instance - self(reference to itself)
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

#Creating instance
celular1 = Celular('Apple', '14 pro max', '100MP')
print(celular1.marca)