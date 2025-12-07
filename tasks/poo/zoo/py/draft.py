

class Animal:
    def __init__(self, nome):
        self.__nome = nome
    
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.__nome}")

    def fazerSom(self):
        return "som"

class Elefante(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazerSom(self):
        return "brummm"


elefante = Elefante("dumbo")
elefante.apresentar_nome()
print (elefante.fazerSom())
    


