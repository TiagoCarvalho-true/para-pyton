class Cliente:
    def __init__(self, nome: str, cpf: str, endereco: str):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def endereco(self):
        return self._endereco