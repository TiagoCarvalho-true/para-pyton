def calculaImposto(salario):
    aliquota:0.00
    if salario >= 0.00  and salario<= 1100:
         aliquota = 0.05
    elif salario>= 1100 and salario <= 1500:
         aliquota = 0.10
    else:
         aliquota =0.15
    return aliquota*salario

valorSalario =float(input("insira o salario aqui: "))
valorBeneficios = float(input("insira o valor dos beneficios aqui: "))

valorImposto = calculaImposto(valorSalario)
saida = valorSalario-valorImposto+valorBeneficios 

print(f' o seu salario final será: {saida}')

         