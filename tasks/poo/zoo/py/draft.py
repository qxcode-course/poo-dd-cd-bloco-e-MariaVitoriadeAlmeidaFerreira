from abc import ABC, abstractmethod;

class Animal(ABC):
    def __init__(self, nome):
        self.__nome = nome
    
    def getNome(self):
        return self.__nome
    
    def apresentar_nome(self):
        print(f"Eu sou {self.__nome}")

    @abstractmethod
    def fazerSom(self):
       pass
       #deve ser implementando nas subclassses
    
    @abstractmethod
    def mover(self):
        pass

class Elefante(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazerSom(self):
        return "brummm"
    
    def mover(self):
        return "passos pesados"
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazerSom(self):
        return "miau miau"
    
    def mover(self):
        return "passos ageis"
    
class Cavalo(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazerSom(self):
        return "iiirrrr"
    
    def mover(self):
        return "pocoto pocoto"


def apresentar(animal = Animal):

    elefante = Elefante("dumbo")
    elefante.apresentar_nome()
    print (elefante.fazerSom())
    print (elefante.mover())

gato = Gato("gato de botas")
gato.apresentar_nome()
print (gato.fazerSom())
print (gato.mover())

cavalo = Cavalo("Pe de pano")
cavalo.apresentar_nome()
print(cavalo.fazerSom())
print(cavalo.mover())


