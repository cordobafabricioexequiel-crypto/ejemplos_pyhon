class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.get_nombre()} {self.apellido} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años.")