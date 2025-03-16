from abc import ABC, abstractclassmethod;

class Transacao(ABC):
    @abstractclassmethod
    def depostar(self,valor:float)->None:
        pass
    
    @abstractclassmethod
    def sacar(self,valor:float)->None:
        pass
    