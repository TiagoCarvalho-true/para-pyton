import random

numero_secreto =random.randint(1,10)

chute = None

while chute!= numero_secreto:
    chute = int(input("Adivinhe o numero:"))
    if chute < numero_secreto:
        print("Muito baixo! Tente novamente")
    elif chute > numero_secreto:
        print("Muito alto! Tente novamente")
    else:
        print("Parabens!!! voce acertou o numero...")