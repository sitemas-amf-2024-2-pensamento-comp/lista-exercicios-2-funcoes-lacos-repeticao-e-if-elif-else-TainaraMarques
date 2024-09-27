def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in texto:
        if letra in vogais:
            contador += 1
            
    return contador

def main():
    frase = input("Digite uma frase: ")
    
    numero_vogais = contar_vogais(frase)
    
    print(f"O número de vogais na frase é: {numero_vogais}")

main()
