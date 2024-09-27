def fibonacci(n):
    fib = []
    a, b = 0, 1  
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b 

    return fib

n = int(input("Digite um número inteiro n para exibir os n primeiros números da sequência de Fibonacci: "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    fibonacci_numeros = fibonacci(n)
    print(f"Os {n} primeiros números da sequência de Fibonacci são: {fibonacci_numeros}")
