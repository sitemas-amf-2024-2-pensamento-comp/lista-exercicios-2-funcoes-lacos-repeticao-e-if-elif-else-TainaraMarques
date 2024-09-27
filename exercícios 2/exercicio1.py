n = int(input("escreva um número positivo: "))

for i in range (n):
    if i % 2 == 0:
        print("Par", i )

    else:
        print("Impares", i)

    i += 1