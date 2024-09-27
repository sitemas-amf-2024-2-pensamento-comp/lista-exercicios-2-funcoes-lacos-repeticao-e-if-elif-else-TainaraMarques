n = int(input("Digite um número: "))

divisor = 1
divisores = []

while divisor <= n:
    if n % divisor == 0:
        divisores.append(divisor)
    divisor+=1

print(divisores)