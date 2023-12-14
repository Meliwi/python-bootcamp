class Metodo:
    def saludar(self, nombre: str) -> None:
        """_summary_

            Método que se accede por clase para saludar
        Args:
            nombre (str): nombre de la persona a saludar
        """
        print(f"Hola, soy un método de clase", nombre)

    # Para acceder a un método de clase se utiliza el decorador @classmethod
    @classmethod    
    def saludar(cls, nombre: str) -> None:
        """_summary_

            Método que se accede por clase para saludar
        Args:
            nombre (str): nombre de la persona a saludar
        """
        print(f"Hola, soy un método de clase", nombre)