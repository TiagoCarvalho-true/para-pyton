def criar_tabela():
    return[[0,0,0]for i in range(3)] 

def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(casa) for casa in linha))

def verifica_vitoria(tabuleiro,jogador):
    for linha in tabuleiro:
       if all(casa==jogador for casa in linha ):
           return True
       
    for coluna in range(3):
        if all(tabuleiro[linha][coluna]==jogador for linha in range(3)):
            return True

    if tabuleiro[0][0] == tabuleiro[1][1]==tabuleiro[2][2]==jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1]== tabuleiro[2][0]==jogador:
        return True
    
    return False

def jogar():
    tabuleiro= criar_tabela()
    jogador = 1

    while True:
        exibe_tabuleiro(tabuleiro)
        linha = int(input(f"Caro Jogador {jogador}, escolha a linha (1 a 3): "))-1
        coluna = int(input(f"Caro Jogador {jogador}, escolha a coluna (1 a 3): "))-1
         
        if tabuleiro[linha][coluna]==0:
           tabuleiro[linha][coluna]=jogador
           if verifica_vitoria(tabuleiro,jogador):
               exibe_tabuleiro(tabuleiro)
               print(f"jogador: {jogador} wins!!!")
               break
           jogador=3-jogador
        else:
            print("Essa posiçao ja esta ocupada. tente novemente.")

if __name__=="__main__":
    jogar()