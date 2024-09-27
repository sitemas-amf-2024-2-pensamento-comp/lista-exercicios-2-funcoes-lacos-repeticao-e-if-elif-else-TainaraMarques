import random

def adivinhar_numero():
    numero_sorteado = random.randint(1, 100)
    tentativas = 0
    print("Tente adivinhar o número entre 1 e 100!")

    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa < numero_sorteado:
            print("Muito baixo! Tente novamente.")
        elif tentativa > numero_sorteado:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {numero_sorteado} em {tentativas} tentativas.")
            break

adivinhar_numero()
