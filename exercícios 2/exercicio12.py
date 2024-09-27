a = int(input("Digite um número: "))

b = int(input("Digite um número: "))

resultado = []

if a > b:
    a, b = b, a

while b >= a:
    soma = b,a + 1
    resultado.append(soma)

print (resultado)