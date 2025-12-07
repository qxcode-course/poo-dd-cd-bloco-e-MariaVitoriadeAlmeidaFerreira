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
        return "voa"
    
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
    
class Lobo(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def fazerSom(self):
        return "auuu baby i'm preying on you tonight"
    
    def mover(self):
        return "like animal"


def apresentar(animal : Animal):

    animal.apresentar_nome()
    print ("Som:", animal.fazerSom())
    print ("Movimentação:", animal.mover())
    print(f"Tipo: {type(animal).__name__}")
    

def main():
    animais = [Elefante("Dumbo"), Gato("Gato de botas"), Cavalo("Pe de Pano"), Lobo("Maroon")]

    for animal in animais:
        apresentar(animal)

main()
    
    #elefante = Elefante("dumbo")
    #elefante.apresentar_nome()
    #print (elefante.fazerSom())
    #print (elefante.mover())

    #gato = Gato("gato de botas")
    #gato.apresentar_nome()
    #print (gato.fazerSom())
    #print (gato.mover())

    #cavalo = Cavalo("Pe de pano")
    #cavalo.apresentar_nome()
    #print(cavalo.fazerSom())
    #print(cavalo.mover())


