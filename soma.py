#Escreva um programa que solicite ao usuário para
#  inserir um número inteiro positivo n e calcule a soma de todos os números inteiros de 1 até n usando um laço while.
n=int(input("insira o valor: "))
soma=0
i=1
while i <= n:
    soma+=i
    i+=1

print(f'a soma de 1 ate {n} e {soma}')