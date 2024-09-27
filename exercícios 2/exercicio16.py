def area(altura,largura):
    a = altura * largura
    return a

def main():
    largura = float(input("Digite a largura da área: "))
    altura = float(input("Digite a altura da área: "))
    a = area(altura,largura)

    print(f"A área do local de acordo com as informações fornessidas é {a}")

main()
