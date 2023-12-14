from decoradores_clases.estaticos import Demo

# Instanciamos la clase: apunta a la dirección de memoria de la clase y 
# permite acceder a los métodos, atributos, etc.
demo = Demo()

# Accedemos al método estático por clase
Demo.saludar_estaticamente("Juan")
# Accedemos al método estático por instancia
demo.saludar("Juan")