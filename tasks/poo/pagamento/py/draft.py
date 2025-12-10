from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor:float, descricao:str):
        self._valor = valor
        self._descricao: str = descricao       
 
    def resumo(self):
        print(f"Pagamento de R$ {self._valor}: {self._descricao}\n")

    def validar_valor(self):
        if self._valor <= 0:
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
        if self._valor > self.__limite_disponivel:
            raise Exception("Fail: limite estourado")
        else:
            self.__limite_disponivel -= self._valor
            print("Pagamento efetuado no Credito")
    
class Pix(Pagamento):
    def __init__(self, valor, descricao, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.__chave: str = chave
        self.__banco: str = banco
    
    def processar(self):
        self.validar_valor()
        print(f"Pix com o valor:{self._valor} efetuado com sucesso para o {self.__chave} para o banco: {self.__banco}")

class Boleto(Pagamento):
    def __init__(self, valor, descricao, codigo_barra: str, vencimento: str):
        super().__init__(valor, descricao)
        self.__codigo_barra: str = codigo_barra
        self.__vencimento: str = vencimento

    def processar(self):
        print ("Boleto gerado. Aguardando pagamento...") 

def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

pagamentos = [
    Pix(150, "Camisa esportiva", "email@ex.com", "Banco XPTO"),
    cartao_de_Credito(400, "Tênis esportivo", "1234 5678 9123 4567", "Cliente X", 500),
    Boleto(89.90, "Livro de Python", "123456789000", "2025-01-10"),
    cartao_de_Credito(800, "Notebook", "9999 8888 7777 6666", "Cliente Y", 700),  # deve falhar
]

for pagamento in pagamentos:
    processar_pagamento(pagamento)