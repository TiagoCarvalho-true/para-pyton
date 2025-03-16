from interfaces.transacao import Transacao
from models.cliente import Cliente
from models.historico import Historico

class Conta(Transacao):
    def __init__(self, cliente: Cliente, numero: int):
        self._saldo = 0
        self._limite = 500
        self._cliente = cliente
        self._numero = numero
        self._historico = Historico()
        self._LIMITE_SAQUES = 3
        self._numero_saques = 0
    
    def depositar(self, valor: float) -> None:
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao("Depósito", valor)
        else:
            raise ValueError("Valor de depósito inválido")
    
    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor de saque inválido")
        
        if self._numero_saques >= self._LIMITE_SAQUES:
            raise ValueError("Limite de saques excedido")
            
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente")
            
        if valor > self._limite:
            raise ValueError("Valor excede o limite por saque")
            
        self._saldo -= valor
        self._numero_saques += 1
        self._historico.adicionar_transacao("Saque", valor)
    
    def get_extrato(self) -> str:
        return self._historico.get_extrato(self._saldo)