from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor:float, descricao:str):
        self.__valor = valor
        self.__descricao: str
    
    def resumo(self):
        print(f"Pagamento de R$ {self.__valor}: {self.__descricao}\n")

    def validar_valor(self,):
        if self.__valor <= 0:
            raise Exception("Fail")
    
    #def processar()
    
class cartao_de_Credito(Pagamento):
    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
        super.()__init__(valor)
