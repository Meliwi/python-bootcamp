class Demo: 
    # Self: referencia a la instancia
    def saludar(self, nombre: str) -> None:
        """_summary_

            Método que se accede por instancia para saludar
        Args:
            nombre (str): nombre de la persona a saludar
        """
        print(f"Hola, soy un método de instancia", nombre)
    
    @staticmethod
    def saludar_estaticamente(nombre: str) -> None:
        """_summary_

            Método que se accede por clase para saludar
        Args:
            nombre (str): nombre de la persona a saludar
        """
        print(f"Hola, soy un método estático", nombre)
