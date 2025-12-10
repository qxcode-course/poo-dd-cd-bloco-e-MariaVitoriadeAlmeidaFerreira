from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float, descricao:str):
        self.__valor = valor
        self.__descricao: str = descricao       
 
    def resumo(self):
        print(f"Pagamento de R$ {self.__valor}: {self.__descricao}\n")

    def validar_valor(self):
        if self.__valor <= 0:
            raise Exception("Fail valor menor que zero")
    
    @abstractmethod
    def processar(self):
        pass
    
class cartao_de_Credito(Pagamento):
    def __init__(self, valor, descricao: str, numero: str, nome_titular: str, limite_disponivel: int):
       super().__init__(valor, descricao)
       self.__numero: str = numero
       self.__nome_titular: str = nome_titular
       self.__limite_disponivel: int = limite_disponivel

    def processar(self):
        if self.__valor > self.__limite_disponivel:
            raise Exception("Fail: limite estourado")
        else:
            self.__limite_disponivel -= self.__valor
            print("Pagamento efetuado no Credito")
    
class Pix(Pagamento):
    def __init__(self, valor, descricao, chave: str, banco: str):
        super().__init__