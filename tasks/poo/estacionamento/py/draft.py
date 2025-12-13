from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id:str, tipo:str):
        self.__id: str = id 
        self._tipo: str = tipo
        self._horaEntrada: int 
    
    def setEntrada(self, horaEntrada:int ) -> None:
        self._horaEntrada = horaEntrada

    def getEntrada(self) -> int:
        return self._horaEntrada
    
    def getTipo(self) -> str:
        return self._tipo
    
    def getId(self) -> str:
        return self.__id
    
    @abstractmethod
    def calcularValor(self, horaSair: int) -> None:
        pass

    def __str__(self) -> str:
        return f"{self._tipo.rjust(10, "_")}: {self.__id.rjust(10, "_")}: {self._horaEntrada}"
    
class Bike(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Bike")
    
    def calcularValor(self, horaSaida:int):
        return 3

class Moto(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Moto")

    def calcularValor(self, horaSaida:int):
        aux = horaSaida - self._horaEntrada
        return aux / 20
    
class Carro(Veiculo):
    def __init__(self, id):
        super().__init__(id, "Carro")

    def calcularValor(self, horaSaida:int):
        aux = horaSaida - self._horaEntrada
        resul = aux / 10
        if resul > 5:
            return resul

class Estacionamento:
    def __init__(self):
        self.__veiculos = list[Veiculo]
        self.__horaAtual:int

    def procurarVeiculo(self, id: str) -> int:
        for i in range(0, len(self.__veiculos)):
            if self.__veiculos[i].getId() == id: 


def main():
    estacionamento = Estacionamento()
    while True:
        linha: str = input()
        print("$" + linha)
        args: list[str] = linha.split("")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
main()