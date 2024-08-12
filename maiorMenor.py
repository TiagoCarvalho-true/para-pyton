n1=int(input("insira o primeiro valor: "))
n2=int(input("insira o segundo valor: "))
n3=int(input("insira o terceiro valor: ")) 

if n1>n2 and n1>n3:
    maior=n1
else:
    if n2>n1 and n2>n3:
        maior=n2
    elif n3>n1 and n3>n2:
        maior=n3


print(maior)