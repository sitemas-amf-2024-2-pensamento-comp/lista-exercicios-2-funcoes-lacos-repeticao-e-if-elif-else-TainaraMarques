lista = [] 

def maior():
    return max(lista)

def menor():
    return min(lista)

def main():
    contador = 0  

    while contador < 5:  
        n = int(input("Digite um número: "))
        lista.append(n)
        contador += 1  
        
    maior_numero = maior()
    menor_numero = menor()

    print(f"O menor número é: {menor_numero}")
    print(f"O maior número é: {maior_numero}")

main()
