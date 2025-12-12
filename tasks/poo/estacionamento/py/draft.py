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
        super().__init__(self, "Moto")

    def calcularValor(self, horaSaida:int):
        aux = horaSaida - self._horaEntrada
        return aux / 20
        