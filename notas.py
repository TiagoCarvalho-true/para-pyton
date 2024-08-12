notas=int(input("insira a notas: "))
soma=0
qtd=0

while notas > 0:
    soma += notas
    qtd += 1
    notas=int(input("insira a notas: "))

media = soma/qtd

if media <= 5 :
    print(f'Sua media foi {media} ,  voce está reprovado')
else:
    if media < 7:
       print(f'Sua media foi {media} ,  voce está em recuperação')
    else:
        print(f'Sua media foi {media} ,  voce esta aprovado pode curtir as ferias')
