from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def adicionar_transacao(self, tipo: str, valor: float) -> None:
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        transacao = f"{tipo}: R$ {valor:.2f} - Data: {data}"
        self._transacoes.append(transacao)
    
    def get_extrato(self, saldo: float) -> str:
        extrato = "\n================ EXTRATO ================\n"
        
        if not self._transacoes:
            extrato += "Não foram realizadas movimentações.\n"
        else:
            for transacao in self._transacoes:
                extrato += f"{transacao}\n"
                
        extrato += f"\nSaldo: R$ {saldo:.2f}"
        extrato += "\n==========================================\n"
        return extrato