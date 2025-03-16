from models.cliente import Cliente
from models.conta import Conta

def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    
    # Criar cliente e conta
    cliente = Cliente("João", "123.456.789-00", "Rua A, 123")
    conta = Conta(cliente, 1)
    
    while True:
        opcao = input(menu)
        
        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
                print("Depósito realizado com sucesso!")
            except ValueError as e:
                print(f"Operação falhou! {str(e)}")
                
        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
                print("Saque realizado com sucesso!")
            except ValueError as e:
                print(f"Operação falhou! {str(e)}")
                
        elif opcao == "e":
            print(conta.get_extrato())
            
        elif opcao == "q":
            print("Obrigado por usar nosso sistema!")
            break
            
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()