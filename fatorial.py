n=int(input("insira o valor para o fatorial: "))
while n < 0:
    n=int(input("Digite um valor valido: "))

fat=1
i=1
while i <= n:
    fat=fat*i
    i=i+1

print(f'o fatorial de {n} e {fat}')
