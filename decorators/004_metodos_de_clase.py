from decoradores_clases.metodos_de_clase import Metodo

# Instanciamos la clase: apunta a la dirección de memoria de la clase y
# permite acceder a los métodos, atributos, etc.
metodo = Metodo()

# Accedemos al método estático por clase
Metodo.saludar("Juan")
# Accedemos al método estático por instancia
metodo.saludar("Juan")