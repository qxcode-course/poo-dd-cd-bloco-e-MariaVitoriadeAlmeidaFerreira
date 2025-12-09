from abc import ABC, abstractmethod


class metodo_Pagamento (ABC):

    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class metodoPix(metodo_Pagamento):
    def __init__ (self, chave: str):
        self.__chave: str = chave 
    
    def processar_pagamento(self, valor: float):
        print(f"pagamento da chave: {self.__chave} no valo:{valor}")


class Pagamento(ABC):
    def __init__(self, valor:float, descricao:str, metodo):
        self.__valor = valor
        self.__descricao: str = descricao
        self.__metodo = metodo
    
    def pagar(self):
        self.__metodo.processar_pagamento(self.__valor)
   
   
    #def resumo(self):
        #print(f"Pagamento de R$ {self.__valor}: {self.__descricao}\n")

    #def validar_valor(self):
        #if self.__valor <= 0:
            #raise Exception("Fail")
    
    #def processar()
    
#class cartao_de_Credito(Pagamento):
#    def __init__(self, valor, descricao, numero, nome_titular, limite_disponivel):
#        super.()__init__(valor)

pix = metodoPix("teste@gmail.com")
pag = Pagamento(11, "teste")
print(pag)
