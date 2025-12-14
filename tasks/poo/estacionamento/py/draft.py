from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id:str, tipo:str):
        self.__id: str = id 
        self._tipo: str = tipo
        self._horaEntrada: int = 0
    
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
        return f"{self._tipo.rjust(10, '_')} : {self.__id.rjust(10, '_')} : {self._horaEntrada}"
    
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
        return 5

class Estacionamento:
    def __init__(self):
        self.__veiculos: list[Veiculo] = []
        self.__horaAtual:int = 0

    def procurarVeiculo(self, id: str) -> int:
        for i in range(0, len(self.__veiculos)):
            if self.__veiculos[i].getId() == id: 
                return i
        return -1
    
    def estacionar(self, veiculo: Veiculo) -> None:
        veiculo.setEntrada(self.__horaAtual)
        self.__veiculos.append(veiculo)

    def pagar(self, id: str) -> None:
        aux = self.procurarVeiculo(id)
        if aux != -1:
            veiculo = self.__veiculos.pop(aux)
            print(f"{veiculo.getTipo()} chegou {veiculo.getEntrada()} saiu {self.__horaAtual}. Pagar R$ {veiculo.calcularValor(horaSaida = self.__horaAtual):_.2f}")

    def passarTempo(self, Tempo: int) -> None:
        self.__horaAtual += Tempo

    def __str__(self) -> str:
        if len(self.__veiculos) != 0:
            return "\n".join(str(x) for x in self.__veiculos) + f"\nHora atual: {self.__horaAtual}"
        else: 
            return f"Hora atual: {self.__horaAtual}"


def main():
    estacionamento = Estacionamento()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(estacionamento)
        elif args[0] == "tempo":
            estacionamento.passarTempo(Tempo = int(args[1]))
        elif args[0] == "estacionar":
            if args[1] == "bike":
                veiculo = Bike(args[2])
                estacionamento.estacionar(veiculo)
            elif args[1] == "moto":
                veiculo = Moto(args[2])
                estacionamento.estacionar(veiculo)
            elif args[1] == "carro":
                veiculo = Carro(args[2])
                estacionamento.estacionar(veiculo)
        elif args[0] == "pagar":
            estacionamento.pagar(args[1])

main()